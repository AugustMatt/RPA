# Robô RPA Challenge 🧠🤖

Este projeto tem como objetivo automatizar o desafio proposto pelo site [RPA Challenge](https://www.rpachallenge.com), que consiste em submeter automaticamente 10 formulários com dados fornecidos pelo próprio site, armazenados em uma planilha Excel.

## 🧩 Desafio

O principal desafio está no mapeamento correto dos elementos da página, uma vez que a cada submissão:
- A posição dos campos no formulário muda.
- Alguns atributos HTML como `id` e `name` também são alterados dinamicamente.

## 🛠 Tecnologias Utilizadas

- **Blue Prism**: Plataforma de automação RPA utilizada para desenvolver o robô.
- **VBO "MS Excel VBO"**: Utilizado para ler os dados da planilha Excel fornecida pelo site.

## 🎥 Demonstração

Um vídeo demonstrando o funcionamento do robô está disponível no YouTube:  
▶️ [Assista aqui](https://youtu.be/iKujnffJZ8g)

## 🚀 Como Usar

1. Abra o Blue Prism.
2. Importe a release `.bprelease`.
3. Certifique-se de que o VBO **MS Excel VBO** está disponível e configurado corretamente.
4. Configure a variável de ambiente chamada **"Caminho arquivo RPA Challenge"** e defina o caminho completo para a planilha Excel.
5. Execute o processo com a planilha fornecida pelo site carregada.

---
