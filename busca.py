import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import openpyxl

    
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.dfimoveis.com.br/aluguel/df/brasilia/apartamento?&ordenamento=mais-recente"
driver.get(url)

arquivoExcel = openpyxl.load_workbook('Apartamentos.xlsx')
planilha = arquivoExcel['Apartamentos']

tamanhoDoResultadoDeBusca = len(driver.find_element(By.ID, 'resultadoDaBuscaDeImoveis').find_elements(By.TAG_NAME, 'a'))

for apartamento in range(tamanhoDoResultadoDeBusca):
    
    #Adcionar a ordem do imóvel no arquivo Excel
    linhaComeco = planilha.max_row + 1
    planilha.cell(row=linhaComeco, column=1).value = apartamento + 1

    #Coletar e adcionar o endereço no arquivo Excel
    endereço = driver.find_elements(By.TAG_NAME, 'h2')[apartamento].text
    planilha.cell(row=linhaComeco, column=2).value = endereço


    #Salvar todas alterações 
    arquivoExcel.save('Apartamentos.xlsx')

valor = ''
valor_por_m2 = ''
area = ''

while True: time.sleep(1000)

