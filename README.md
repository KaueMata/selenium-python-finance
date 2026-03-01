Automação de Transações: Do Cypress ao Selenium com Python 🚀
Este projeto foi desenvolvido para praticar a transição da automação de testes do ecossistema JavaScript (Cypress) para o Selenium WebDriver com Python. O objetivo principal foi automatizar o fluxo de cadastro de transações em uma aplicação financeira (Dev.Finance).

📌 Sobre o Projeto
O script realiza o acesso ao site, interage com modais e preenche múltiplos formulários de forma rápida e eficiente.

O que foi praticado:
Mapeamento de Elementos: Uso de ID para campos de entrada (description, amount, date) e XPath com contains para capturar o botão de abertura do modal e o botão de salvar.

Interação Dinâmica: Captura de botões que não possuem IDs fixos, utilizando o texto visível no DOM.

Refatoração (Função + Loop): O código foi estruturado em uma função, eliminando a repetição manual de blocos de código e permitindo realizar vários cadastros sequenciais de forma limpa.

🛠️ Tecnologias Utilizadas
Python

Selenium WebDriver

Microsoft Edge Driver (configurado via webdriver.Edge())

🚀 Como rodar o projeto
Clone o repositório:

Bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Instale o Selenium:

Bash
pip install selenium
Execute o script:

Bash
python mainS1.py
📝 Lições Aprendidas
A principal diferença notada em relação ao Cypress foi o controle manual sobre o fluxo de execução. Enquanto o Cypress gerencia esperas automaticamente, o Selenium exige uma definição clara de como e quando interagir com cada elemento. A criação de funções para automatizar tarefas repetitivas tornou o script muito mais organizado e fácil de manter.
