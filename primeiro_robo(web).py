import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def digitacao_humana(elemento, texto):
    """Simula a digitação de uma pessoa, caractere por caractere."""
    for letra in texto:
        elemento.send_keys(letra)
        time.sleep(random.uniform(0.1, 0.2))

print("--- Iniciando o Robô (Google -> YouTube -> Cursos de Rede) ---")

# 1. Configurações para suavizar a detecção E MANTER O NAVEGADOR ABERTO
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # <-- Impede o Chrome de fechar ao término
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

# Passo 1: Abrir o Google
print("1. Abrindo o Google...")
driver.get("https://www.google.com")
time.sleep(2)

# Passo 2: Pesquisar por "YouTube" no Google
print("2. Pesquisando por 'YouTube' no Google...")
campo_busca_google = driver.find_element(By.NAME, "q")
digitacao_humana(campo_busca_google, "YouTube")
campo_busca_google.send_keys(Keys.ENTER)
time.sleep(3)

# Passo 3: Clicar no primeiro resultado do YouTube no Google
print("3. Entrando no site do YouTube...")
link_youtube = driver.find_element(By.XPATH, '//h3[contains(text(), "YouTube")]')
link_youtube.click()
time.sleep(4)

# Passo 4: Localizar a barra de pesquisa DO YOUTUBE e pesquisar o curso
print("4. Localizando a barra de pesquisa do YouTube...")
campo_busca_yt = driver.find_element(By.NAME, "search_query")
campo_busca_yt.click()

termo_curso = "curso de redes de computadores"
print(f"5. Digitando no YouTube: '{termo_curso}'...")
digitacao_humana(campo_busca_yt, termo_curso)
time.sleep(1)
campo_busca_yt.send_keys(Keys.ENTER)

print("\n--- Processo concluído! A janela do navegador permanecerá aberta. ---")