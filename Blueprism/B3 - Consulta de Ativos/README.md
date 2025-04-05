

# 🤖 B3 - Consulta de Ativos (Blue Prism)

Este robô foi desenvolvido na versão **7.4 do Blue Prism**, como parte do curso **"Blueprism do básico ao avançado"** do canal [RPA Hour](https://www.youtube.com/@rpahour), ministrado por **Davi Arndt**. Representa meu primeiro contato com a ferramenta Blue Prism.

## 📌 Objetivo

Automatizar a consulta de ativos no site da **B3** e retornar informações como:

- Preço do ativo
- Oscilação
- Data e hora da última atualização
- Data da consulta realizada pelo robô

Esses dados são extraídos de uma planilha Excel e, ao final do processo, os resultados atualizados são enviados por e-mail.

> O projeto foi estruturado utilizando **filas (queues)** do Blue Prism, podendo ser adaptado para execução em **estrutura multibot**.

---

## ⚙️ Funcionamento

1. O robô lê uma planilha Excel com uma lista de códigos de ativos.
2. Acessa o site da B3:
   [https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/outros-ativos.htm](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/outros-ativos.htm)
3. Realiza a busca de cada ativo.
4. Extrai os dados necessários.
5. Preenche novamente a planilha com os dados coletados.
6. Envia a planilha atualizada por e-mail.

---

## 📁 Estrutura da Planilha

A planilha Excel deve conter a seguinte estrutura:

| Ativo | Preço | Data | Hora | Data Consulta Robô |
|-------|-------|------|------|---------------------|
| PETR4 |       |      |      |                     |
| VALE3 |       |      |      |                     |
| ...   |       |      |      |                     |

> Apenas a coluna **A (Ativo)** deve estar preenchida inicialmente. As demais serão preenchidas automaticamente pelo robô.

---

## 📦 Requisitos

### VBOs necessários

- [Email - POP3/SMTP/IMAP](https://digitalexchange.blueprism.com/cardDetails?id=115178)
- [MS Excel VBO](https://digitalexchange.blueprism.com/cardDetails?id=115181)
- [Utility - General](https://digitalexchange.blueprism.com/cardDetails?id=115169)

### Variáveis de Ambiente

- `Caminho Arquivo - Ativos`: Caminho completo para a planilha Excel utilizada no processo.

### Credenciais (Credentials)

- `B3 Consulta de Ativos - Email Remetente`: E-mail e senha utilizados para envio.
- `B3 Consulta de Ativos - Email Destinatario`: E-mail que receberá a planilha atualizada.

### Queue

- `B3 - Consulta de Ativos`: Queue utilizada pelo processo para gerenciar os itens.

---

## 📝 Observações

Este projeto tem fins **educacionais** e foi criado durante um curso introdutório à ferramenta Blue Prism. Algumas melhorias e adaptações podem ser realizadas para aplicações em ambientes produtivos.

---

## 📷 Créditos

Curso: **Blueprism do básico ao avançado**  
Canal: [RPA Hour - Davi Arndt](https://www.youtube.com/@rpahour)
