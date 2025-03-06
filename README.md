<p align="center">
  <img src="https://t4.ftcdn.net/jpg/03/48/80/11/360_F_348801155_mjJdt25Vkap8MSgxgMbmOYmdn5JdCfvp.jpg" alt="CodeAPI Banner" width="600" style="border-radius: 10px;"/>
</p>

<h1 align="center">💸 CodeAPI - Payment Links Gen</h1>
<p align="center">
  <strong>Uma ferramenta simples e poderosa para gerar links de pagamento Pix de forma rápida e prática.</strong><br>
  Desenvolvido por <a href="https://github.com/LucasDesignerF">LucasDesignerF</a> | Parte do <a href="https://discord.gg/x74fnzcz2S">CodeProjects</a>
</p>

<p align="center">
  <a href="https://codeapi-pay.redebots.shop/"><img src="https://img.shields.io/badge/Website-Live-brightgreen?style=for-the-badge&logo=internet-explorer" alt="Website Live"/></a>
  <a href="https://github.com/LucasDesignerF/codeapi-pay-gen"><img src="https://img.shields.io/github/stars/LucasDesignerF/codeapi-pay-gen?style=for-the-badge&logo=github&color=yellow" alt="GitHub Stars"/></a>
  <a href="https://github.com/LucasDesignerF/codeapi-pay-gen/fork"><img src="https://img.shields.io/github/forks/LucasDesignerF/codeapi-pay-gen?style=for-the-badge&logo=github&color=orange" alt="GitHub Forks"/></a>
  <a href="https://github.com/LucasDesignerF/codeapi-pay-gen/issues"><img src="https://img.shields.io/github/issues/LucasDesignerF/codeapi-pay-gen?style=for-the-badge&logo=github&color=red" alt="GitHub Issues"/></a>
  <a href="https://discord.gg/x74fnzcz2S"><img src="https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord" alt="Join Discord"/></a>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status Active"/>
  <img src="https://img.shields.io/badge/Version-1.1.0-blue?style=for-the-badge" alt="Version 1.1.0"/>
</p>

---

## 🚀 Sobre o Projeto

O **CodeAPI - Payment Links Gen** é uma aplicação web estática que permite criar links de pagamento Pix de forma descomplicada. Insira os dados do produto, gere um link personalizado e compartilhe com qualquer pessoa para facilitar transações via Pix. Tudo isso com um design moderno, tema escuro e suporte a QR Codes!

### 🎯 Funcionalidades Principais
- **Geração de Links Pix**: Crie links de pagamento com chave Pix, produto, descrição, valor e imagem.
- **Visualização Detalhada**: Cada link leva a uma página com os detalhes do pagamento, incluindo QR Code e payload para copiar.
- **Layout Moderno**: Informações do produto e pagamento organizadas em cards lado a lado para melhor visualização.
- **Tema Escuro**: Interface estilizada com tons de verde dólar, inspirada no modo escuro do PicPay.
- **Responsivo**: Funciona perfeitamente em dispositivos móveis e desktops.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia       | Descrição                      |
|------------------|--------------------------------|
| **HTML5**        | Estrutura da aplicação         |
| **TailwindCSS**  | Estilização moderna via CDN    |
| **JavaScript**   | Lógica dinâmica com jQuery     |
| **Font Awesome** | Ícones personalizados via CDN  |
| **QRCode.js**    | Geração de QR Codes no cliente |
| **JSONBin.io**   | Armazenamento temporário       |

---

## 📋 Como Usar

1. **Acesse o site**: Visite [https://codeapi-pay.redebots.shop/](https://codeapi-pay.redebots.shop/) ou clone o repositório e abra localmente.
2. **Preencha os dados**:
   - Chave Pix (ex.: e-mail, CPF, etc.)
   - Nome do produto
   - Descrição (identificador, máx. 10 caracteres)
   - Valor em reais
   - (Opcional) URL de uma imagem do produto
3. **Gere o link**: Clique em "Gerar Link de Pagamento".
4. **Compartilhe**: Copie o link gerado e envie para quem precisa pagar.
5. **Visualize**: O destinatário verá os detalhes do pagamento, incluindo QR Code e payload Pix.

> **Nota**: Os links gerados são armazenados temporariamente no JSONBin.io. Não há persistência permanente sem um backend completo.

---

## 🖼️ Screenshots

<p align="center">
  <img src="https://media.discordapp.net/attachments/1343354778574389299/1347029890062356501/image.png?ex=67ca56d8&is=67c90558&hm=87af4bab4b32f44756cdd1539600c8a8b4bcab7e69cfbdafd339587285fe403c&=&format=webp&quality=lossless&width=985&height=554" alt="Página Inicial" width="300"/>
  <img src="https://media.discordapp.net/attachments/1343354778574389299/1347030509498273854/image.png?ex=67ca576c&is=67c905ec&hm=2f7d62ac42a882ae5996046584e727df8be34b851584fabbf945e765f512da0c&=&format=webp&quality=lossless&width=985&height=554" alt="Detalhes do Pagamento" width="300"/>
  <img src="https://media.discordapp.net/attachments/1343354778574389299/1347030739665031239/image.png?ex=67ca57a2&is=67c90622&hm=7a5f839b753cc63a7ea32fd88656cc90395b07093fb18f0a60430a1f2b88b1f1&=&format=webp&quality=lossless&width=985&height=554" alt="Sobre a Plataforma" width="300"/>
</p>

*(Substitua os placeholders acima por capturas de tela reais do projeto! Recomendo usar ferramentas como Lightshot ou ShareX para capturar e hospedar as imagens no GitHub ou Imgur.)*

---

## 🤝 Contribuição

Quer ajudar a melhorar o projeto? Siga estes passos:

1. Faça um fork do repositório: [https://github.com/LucasDesignerF/codeapi-pay-gen](https://github.com/LucasDesignerF/codeapi-pay-gen).
2. Crie uma branch para sua feature (`git checkout -b feature/nova-ideia`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova ideia'`).
4. Envie para o repositório remoto (`git push origin feature/nova-ideia`).
5. Abra um Pull Request e descreva suas mudanças.

---

## 📡 Suporte e Comunidade

Junte-se ao nosso servidor no Discord para tirar dúvidas, sugerir melhorias ou apenas conversar sobre o projeto!

<p align="center">
  <a href="https://discord.gg/x74fnzcz2S"><img src="https://img.shields.io/badge/Discord-CodeProjects-7289DA?style=for-the-badge&logo=discord" alt="Join Discord"/></a>
</p>

---

## 📜 Licença

Este projeto é licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<h3 align="center">💻 Feito com 💚 por LucasDesignerF</h3>
<p align="center">
  Parte do ecossistema <a href="https://discord.gg/x74fnzcz2S">CodeProjects</a>
</p>
