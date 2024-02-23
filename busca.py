import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

    
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.dfimoveis.com.br/aluguel/df/brasilia/apartamento"
driver.get(url)

teste = driver.find_elements(By.CSS_SELECTOR, 'option.ordenamento[value="mais-recente"]')

while True: time.sleep(1000)

