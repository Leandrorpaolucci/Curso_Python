from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

try:
    navegador.maximize_window()
    navegador.get("https://web.whatsapp.com/")

    

    # Aguardar indefinidamente para manter o navegador aberto
    while True:
        sleep(10)  # Aguarda 10 segundos antes de repetir o loop

except KeyboardInterrupt:
    # Captura a interrupção de teclado (Ctrl+C) para encerrar o programa
    pass

finally:
    navegador.quit()
