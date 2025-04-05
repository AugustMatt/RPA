# NET/Claro Residencial - Emitir Fatura

## Descrição

Este projeto é um robô desenvolvido em **Blue Prism (versão 7.4)** para automatizar o processo de emissão de faturas do site **Minha NET/Claro Residencial**. O bot realiza as seguintes etapas:

1. Acessa o site **Minha NET/Claro Residencial**;
2. Realiza login utilizando credenciais seguras;
3. Emite e baixa a fatura;
4. Realiza logoff;
5. Envia a fatura por e-mail para um destinatário predefinido.

---

## 🎥 Demonstração

Confira abaixo um vídeo demonstrando a automação em funcionamento:

[![Assista à demonstração no YouTube](https://img.youtube.com/vi/rdILDB0sc5k/0.jpg)](https://www.youtube.com/watch?v=rdILDB0sc5k)

---

## Requisitos

### 1. Dependências (VBOs)
Para o funcionamento do robô, é necessário importar os seguintes **VBOs** disponíveis no **Blue Prism Digital Exchange**:

- **Email - POP3/SMTP/IMAP**: [Download](https://digitalexchange.blueprism.com/cardDetails?id=115178)
- **Utility - File Management**: [Download](https://digitalexchange.blueprism.com/cardDetails?id=115161)
- **Utility - General**: [Download](https://digitalexchange.blueprism.com/cardDetails?id=115169)
- **Utility - Environment**: [Download](https://digitalexchange.blueprism.com/cardDetails?id=115160)

Cada VBO pode possuir dependências específicas que devem ser verificadas diretamente em suas respectivas páginas de download.

---

### 2. Credenciais no Blue Prism
Para garantir a segurança dos dados de acesso, o bot utiliza credenciais armazenadas de forma segura no **Blue Prism**. As seguintes credenciais devem ser configuradas:

- **NET/Claro Residencial**:
  - `Username`: Nome de usuário para login no site;
  - `Password`: Senha de acesso ao site.

- **NET/Claro Residencial Email Remetente**:
  - `Username`: Endereço de e-mail utilizado para envio da fatura;
  - `Password`: Senha do e-mail remetente (conforme regras do provedor).

- **NET/Claro Residencial Email Destinatário**:
  - `Username`: Endereço de e-mail que receberá a fatura. **(Não necessita de senha)**.

Também é necessário configurar corretamente os acessos de usuários, processos e recursos para que o bot possa utilizar essas credenciais.

---

### 3. Configurações Internas da VBO
O bot utiliza algumas variáveis internas configuradas na página **"Initialise"** da **VBO**:

- **Chrome Executable Path**: Caminho do executável do **Google Chrome**;
- **NET/CLARO URL**: Link da página inicial do site **Minha NET/Claro Residencial**;
- **Temp Download Folder**: Pasta temporária criada para armazenar a fatura durante a execução;
- **Chrome User Data Path**: Caminho do perfil exclusivo do Chrome para execução do bot;
- **Chrome Profile Name**: Nome do perfil utilizado pelo Chrome.

**Importante:** O perfil do Chrome deve estar configurado para que a pasta de downloads seja a mesma definida em **"Temp Download Folder"**.

---

### 4. Outros Parâmetros

O bot também possui outras configurações, como **número de tentativas**, **tempo de espera**, entre outros, que podem ser ajustados conforme necessidade, mas **não são requisitos obrigatórios** para o funcionamento padrão.

---

## Como Executar

1. Configure todas as credenciais no **Blue Prism**;
2. Importe e configure os VBOs necessários;
3. Ajuste os caminhos e variáveis na página **Initialise**;
4. Execute o processo principal.

---

## Autor
Matheus Amaral - RPA Developer

Se precisar de ajustes ou melhorias, fique à vontade para contribuir! 🚀
