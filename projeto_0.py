from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pointer

cep_list = [75660000, 75650000, 75503020]
cep_extract = []
navegador = webdriver.Chrome()

try:
    navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    for cep in cep_list:
        navegador.find_element(By.NAME, 'endereco').send_keys(cep)
        navegador.find_element(By.NAME, 'btn_pesquisar').click()
        pointer.sleep(1)
        extracao = {
            'logradouro': navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text,
            'bairro': navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text,
            'cidade': navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text,
        }

        extracao = {chave: valor for chave, valor in extracao.items() if valor != ''}
        cep_extract.append(extracao)
        pointer.sleep(1)
        navegador.find_element(By.ID, 'btn_nbusca').click()

except Exception as e:
    print(e)


print(*cep_extract, sep='\n')