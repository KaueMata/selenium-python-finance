from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Edge()
navegador.get("https://dev-finance.netlify.app/#")

def adicionar_transacao(descricao, valor_item, data_item):
    navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()
    navegador.find_element("id", "description").send_keys(descricao)
    navegador.find_element("id", "amount").send_keys(valor_item)
    navegador.find_element("id", "date").send_keys(data_item)
    navegador.find_element("xpath", "//button[text()='Salvar']").click()
    time.sleep(1)

adicionar_transacao("Orçamento", "3200", "01/03/2026")
adicionar_transacao("Monitor", "-700", "01/04/2027")
adicionar_transacao("DDR3", "-500", "01/04/2026")
adicionar_transacao("SSD", "-700", "01/04/2026")
adicionar_transacao("RTX 3050", "-1200", "01/04/2026")