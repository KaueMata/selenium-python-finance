from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# acessar um site
navegador = webdriver.Edge()
navegador.get("https://dev-finance.netlify.app/#")
#navegador.maximize_window()

# Usa o contains para não ter erro com o símbolo de "+" ou espaços
navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()

campo_descricao = navegador.find_element("id", "description")
campo_descricao.send_keys("Orçamento")

valor = navegador.find_element("id", "amount")
valor.send_keys("3200")

data = navegador.find_element("id", "date")
# formato dd/mm/aaaa  
data.send_keys("01/03/2026")

navegador.find_element("xpath", "//button[text()='Salvar']").click()



# Usa o contains para não ter erro com o símbolo de "+" ou espaços
navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()

campo_descricao = navegador.find_element("id", "description")
campo_descricao.send_keys("Monitor")

valor = navegador.find_element("id", "amount")
valor.send_keys("-700")

data = navegador.find_element("id", "date")
# formato dd/mm/aaaa  
data.send_keys("01/04/2027")

navegador.find_element("xpath", "//button[text()='Salvar']").click()
time.sleep(1)




# Usa o contains para não ter erro com o símbolo de "+" ou espaços
navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()

campo_descricao = navegador.find_element("id", "description")
campo_descricao.send_keys("DDR3")

valor = navegador.find_element("id", "amount")
valor.send_keys("-500")

data = navegador.find_element("id", "date")
# formato dd/mm/aaaa  
data.send_keys("01/04/2026")

navegador.find_element("xpath", "//button[text()='Salvar']").click()
time.sleep(1)








# Usa o contains para não ter erro com o símbolo de "+" ou espaços
navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()

campo_descricao = navegador.find_element("id", "description")
campo_descricao.send_keys("SSD")

valor = navegador.find_element("id", "amount")
valor.send_keys("-700")

data = navegador.find_element("id", "date")
# formato dd/mm/aaaa  
data.send_keys("01/04/2026")

navegador.find_element("xpath", "//button[text()='Salvar']").click()
time.sleep(1)

# Usa o contains para não ter erro com o símbolo de "+" ou espaços
navegador.find_element("xpath", "//*[contains(text(), 'Nova Transação')]").click()

campo_descricao = navegador.find_element("id", "description")
campo_descricao.send_keys("DRTX 3050")

valor = navegador.find_element("id", "amount")
valor.send_keys("-1200")

data = navegador.find_element("id", "date")
# formato dd/mm/aaaa  
data.send_keys("01/04/2026")

navegador.find_element("xpath", "//button[text()='Salvar']").click()
time.sleep(10)


