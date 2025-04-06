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

<a href="https://www.youtube.com/watch?v=rdILDB0sc5k" target="_blank">
  <img src="https://img.youtube.com/vi/rdILDB0sc5k/0.jpg" alt="Assista à demonstração no YouTube" />
</a>

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

---

### 3. Environment Variables

As variáveis globais utilizadas pelo bot foram movidas para o ambiente (**Environment Variables**), facilitando a manutenção e configuração do processo:

- **Chrome User Data Path**: Caminho para a pasta de perfis do Chrome.
- **URL Minha NET/Claro Residencial**: Link da página inicial do site.

---

### 4. Configurações no Processo Principal

A lógica de manipulação de arquivos e pastas foi movida do VBO para o **processo principal**, garantindo melhor separação de responsabilidades. As seguintes variáveis foram adicionadas:

- **Chrome Nome Perfil**: Nome do perfil do Chrome configurado para realizar os downloads na pasta correta.
- **Caminho Pasta Download Temporario**: Pasta temporária gerenciada pelo processo para armazenar a fatura durante a execução.

**Importante:** Certifique-se de que o perfil do Chrome esteja configurado para utilizar a pasta de downloads definida em `Caminho Pasta Download Temporario`.

---

### 5. Outros Parâmetros

O bot também possui outras configurações ajustáveis, como **número de tentativas**, **tempo de espera**, entre outros — que não são obrigatórios para o funcionamento básico.

---

## Como Executar

1. Configure todas as credenciais no **Blue Prism**;
2. Importe e configure os VBOs necessários;
3. Defina as **Environment Variables**;
4. Ajuste o nome do perfil e a pasta de download no processo principal;
5. Execute o processo principal.

---

## Autor

Matheus Amaral - RPA Developer

Se precisar de ajustes ou melhorias, fique à vontade para contribuir! 🚀
