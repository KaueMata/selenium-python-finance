Automação de Transações: Do Cypress ao Selenium com Python 🚀
Este projeto foi desenvolvido para praticar a transição da automação de testes do ecossistema JavaScript (Cypress) para o Selenium WebDriver com Python. O objetivo principal foi automatizar o fluxo de cadastro de transações em uma aplicação financeira.

📌 Sobre o Projeto
O script realiza o acesso ao site, interage com modais e preenche formulários de forma automatizada.

O que foi praticado:
Mapeamento de Elementos: Uso de ID para campos de entrada e XPath com contains para botões dinâmicos, garantindo seletores mais robustos.

Refatoração: O código evoluiu de uma estrutura sequencial para o uso de funções parametrizadas, permitindo a reutilização da lógica e a execução de múltiplos cadastros via loop.

Segurança: Implementação de variáveis de ambiente (.env) para gerenciar credenciais de acesso de forma segura.

🛠️ Tecnologias Utilizadas
Python

Selenium WebDriver

Microsoft Edge Driver (configurado para webdriver.Edge())

Python-dotenv (para gestão de variáveis de ambiente)

🚀 Como rodar o projeto
Clone o repositório:

Bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
Instale as dependências:

Bash
pip install selenium python-dotenv
Configure as credenciais:
Crie um arquivo .env na raiz do projeto seguindo o modelo:

Plaintext
USER_EMAIL=seu_email@exemplo.com
SENHA_USER=sua_senha_aqui
Execute o script:

Bash
python mainS1.py
📝 Lições Aprendidas
Diferente do Cypress, que possui esperas automáticas (auto-wait), o Selenium exigiu um controle mais granular do tempo de renderização e da hierarquia do DOM. A transição permitiu entender melhor como o WebDriver interage diretamente com o navegador e como estruturar automações modulares em Python.
