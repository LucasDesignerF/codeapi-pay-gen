function calculateCRC16(data) {
    let crc = 0xFFFF;
    const polynomial = 0x1021;

    for (let char of data) {
        crc ^= (char.charCodeAt(0) << 8);
        for (let i = 0; i < 8; i++) {
            if (crc & 0x8000) {
                crc = (crc << 1) ^ polynomial;
            } else {
                crc <<= 1;
            }
            crc &= 0xFFFF;
        }
    }

    return crc.toString(16).padStart(4, '0').toUpperCase();
}

function addField(id, value) {
    if (value === null || value === undefined) return '';
    const valueStr = String(value);
    const length = valueStr.length.toString().padStart(2, '0');
    return id + length + valueStr;
}

function generatePixPayload(chavePix, valor, txid = '***', nomeMerchant = 'N', cidadeMerchant = 'C') {
    let payload = '';

    payload += addField('00', '01'); // Payload Format Indicator

    const merchantAccount = `0014BR.GOV.BCB.PIX01${chavePix.length.toString().padStart(2, '0')}${chavePix}`;
    payload += addField('26', merchantAccount);

    payload += addField('52', '0000'); // Merchant Category Code
    payload += addField('53', '986');  // Transaction Currency

    if (valor !== null && valor > 0) {
        const valorStr = valor.toFixed(2);
        payload += addField('54', valorStr); // Transaction Amount
    }

    payload += addField('58', 'BR'); // Country Code
    payload += addField('59', nomeMerchant); // Merchant Name
    payload += addField('60', cidadeMerchant); // Merchant City

    const txidField = `05${txid.length.toString().padStart(2, '0')}${txid}`;
    payload += addField('62', txidField); // Additional Data Field

    const payloadWithoutCRC = payload + '6304';
    const crc = calculateCRC16(payloadWithoutCRC);
    const payloadComplete = payloadWithoutCRC + crc;

    return payloadComplete;
}

// Nota: A geração do QR Code é feita no lado do cliente (em payment.html) usando QRCode.js,
// replicando as configurações do Python (version=1, error_correction=M, box_size=10, border=4).