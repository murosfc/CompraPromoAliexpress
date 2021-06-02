from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selecionar_pagamento():
    driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/button').click()  # clica em selecionar boleto
    driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/div').click()  # clica em boleto
    driver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[3]/div[2]/button').click()  # clica em confirmar método de pagamento

def finalizar_compra():
    driver.find_element_by_xpath(
        '//*[@id="price-overview"]/div[1]/div/div/div[1]/div[3]/div/form/div[2]/div/button').click()  # clica confirmar cupom
    driver.find_element_by_xpath('//*[@id="checkout-button"]').click()  # clica em fazer pedido
    driver2.quit()
    print("Comprado com sucesso Encerre a Janela do navegador manualmente")


link = input("Digite o link da promoção do Aliexpress")
driver = webdriver.Chrome()
driver.get(link)
print("\n\nFaça o login, escolha o modelo e deixe na tela do check-out")
selecionar_pagamento()
cupom = input("digite o cupom")
driver.find_element_by_id('code').send_keys(cupom)  # insere cupom
driver2 = webdriver.Chrome()
driver2.get('https://time.is/pt_br/Bras%C3%ADlia')

while true:
    hms = driver2.find_element_by_xpath('//*[@id="clock"]').text  # pega hora minuto e segundo
    hora = int(hms[0] + hms[1])
    # minuto = int (hms[3]+hms[4])
    segundo = int(hms[6] + hms[7])
    if (hora >= 21 and segundo >= 0):
        finalizar_compra()
        break
