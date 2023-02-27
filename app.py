from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

# Esse Script abre o 10FastFingers.com no Chrome e digita automaticamente todas as palavras.
# Feito com o intuito de aprender mais sobre Web Scraping com Python.

driver = webdriver.Chrome()
# Abrindo o site no navegador
driver.get('https://10fastfingers.com/typing-test/portuguese')                                     

pyautogui.alert(text='Pronto?', title='Hack Typing Alert', button='Ok')

cont = True
while cont:
    # Input das palavras do site
    inputwords = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input')

    # Elemento com todas a palavras 
    wordslist = driver.find_element(By.XPATH, "//*[@id='row1']")

    # Cada palavra da lista de palavras
    word = wordslist.find_elements(By.TAG_NAME, "span")
    
    # Para cada palavra
    for w in word:
        # Digitando no campo de texto a palavra
        inputwords.send_keys(w.text + " ")

    # Caixa de texto para saber se quer tentar de novo
    c = pyautogui.confirm(text='Quer ir de novo?', title='Hack Typing Alert', buttons=['Sim', 'Nao'])
    if c == 'Nao':
        cont = False

# Tira uma screenshot da tela e salva no diretorio do app.py
driver.save_screenshot('screenshot.png')
driver.close()
