# 🤖 Unimed Invoice Automation

Este projeto é uma automação em Python com Selenium para realizar o login no portal da Unimed Natal, verificar se há faturas disponíveis, baixar a fatura (em PDF) e enviar por email. Também trata exceções, re-tentativas e notificações em caso de erro.

## 📌 Funcionalidades

- Login automatizado no portal da Unimed Natal
- Detecção de credenciais inválidas
- Verificação de faturas disponíveis
- Download automático da fatura em PDF
- Envio por email com ou sem anexo
- Re-tentativas automáticas em caso de falhas temporárias
- Notificação por email em caso de erro crítico

## 🚀 Tecnologias Utilizadas

- Python 3
- Selenium
- Python-dotenv
- SMTP (envio de email)

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/AugustMatt/RPA.git
   cd RPA/Python/Unimed\ Natal\ -\ Emitir\ Fatura
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` com suas credenciais:
   ```env
   LOGIN=seu_login
   PASSWORD=sua_senha
   SENDER_MAIL=seu_email@gmail.com
   SENDER_PASS=sua_senha_de_aplicativo
   RECEIVERS_MAILS=destinatario1@gmail.com,destinatario2@gmail.com
   ```

Atenção: Use uma senha de aplicativo para contas Google com autenticação em dois fatores.

## 📁 Estrutura do Projeto

```
unimed-invoice-bot/
├── driver.py
├── invoice.py
├── navigation.py
├── send_email.py
├── utils.py
├── config.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## 🛠️ Execução

Com o ambiente ativado, basta rodar:

```bash
python main.py
```

O script tentará no máximo 3 vezes em caso de falha temporária. Se as credenciais forem inválidas ou ocorrer erro em todas as tentativas, um email será enviado informando o ocorrido.

## 📹 Demonstração

Em breve será adicionado um vídeo de demonstração desta automação em funcionamento.

## 🧾 Licença

Este projeto é de uso pessoal e educativo.

---
