import json
import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify
import qrcode
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

# Caminho para o arquivo JSON de armazenamento
DATA_FILE = "data/payments.json"

# Cria o arquivo JSON se não existir
if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump({}, f)

# Classe GeradorPix adaptada para o Flask
class GeradorPix:
    def __init__(self):
        self.payload = {}
    
    def _adicionar_valor(self, id_campo, valor):
        if valor is not None:
            valor_str = str(valor)
            tamanho = f"{len(valor_str):02d}"
            self.payload[id_campo] = id_campo + tamanho + valor_str
    
    def calculate_crc16(self, data):
        crc = 0xFFFF
        polynomial = 0x1021
        for byte in data.encode('ascii'):
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ polynomial
                else:
                    crc <<= 1
                crc &= 0xFFFF
        return f"{crc:04X}"

    def gerar_payload(self, chave_pix, valor=None, txid="***", nome_merchant="N", cidade_merchant="C"):
        self.payload = {}
        self._adicionar_valor("00", "01")  # Payload Format Indicator
        merchant_account = f"0014BR.GOV.BCB.PIX01{len(chave_pix):02d}{chave_pix}"
        self._adicionar_valor("26", merchant_account)
        self._adicionar_valor("52", "0000")  # Merchant Category Code
        self._adicionar_valor("53", "986")   # Transaction Currency
        if valor is not None and valor > 0:
            valor_str = f"{valor:.2f}"
            self._adicionar_valor("54", valor_str)  # Transaction Amount
        self._adicionar_valor("58", "BR")    # Country Code
        self._adicionar_valor("59", nome_merchant)  # Merchant Name
        self._adicionar_valor("60", cidade_merchant)  # Merchant City
        txid_field = f"05{len(txid):02d}{txid}"
        self._adicionar_valor("62", txid_field)
        payload_sem_crc = ''.join(self.payload.values()) + "6304"
        crc_hex = self.calculate_crc16(payload_sem_crc)
        payload_completo = payload_sem_crc + crc_hex
        return payload_completo
    
    def gerar_qrcode_base64(self, payload, size=300):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size), Image.LANCZOS)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{img_str}"

# Função para carregar dados do arquivo JSON
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Função para salvar dados no arquivo JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Rota principal (index)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota para criar um novo link de pagamento
@app.route('/create', methods=['POST'])
def create_payment():
    data = request.form
    chave_pix = data['chavePix']
    produto = data['produto']
    descricao = data['descricao'].upper().replace('[^A-Z0-9]', '')[:10]  # Sanitiza a descrição
    valor = float(data['valor'])
    imagem = data.get('imagem', '')

    gerador = GeradorPix()
    payload = gerador.gerar_payload(chave_pix, valor, descricao)

    # Gera um ID único para o pagamento
    record_id = str(uuid.uuid4())
    payment_data = {
        "chavePix": chave_pix,
        "produto": produto,
        "descricao": descricao,
        "valor": valor,
        "imagem": imagem,
        "payload": payload
    }

    # Salva no arquivo JSON
    payments = load_data()
    payments[record_id] = payment_data
    save_data(payments)

    return jsonify({"recordId": record_id})

# Rota para visualizar detalhes do pagamento
@app.route('/payment/<record_id>')
def payment(record_id):
    payments = load_data()
    data = payments.get(record_id)

    if not data:
        return render_template('payment.html', error="Pagamento não encontrado.")

    gerador = GeradorPix()
    qr_code_base64 = gerador.gerar_qrcode_base64(data['payload'], size=300)

    return render_template('payment.html', data=data, qr_code=qr_code_base64)

if __name__ == "__main__":
    app.run(debug=True)