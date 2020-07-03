from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class CursoAutomacao:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        self.driver.get('http://www.waves.com.br')
        self.driver.maximize_window()
        self.pergunta = input("Qual praia vocês deseja verificar a previsão do mar? Joaquina, Mole, Campeche, Vila,Porto, Rosa Sul, Rosa Norte, Ribanceira ?")
        time.sleep(15)

        botao_wavescheck = self.driver.find_element_by_class_name("sf-with-ul")
        time.sleep(5)
        botao_wavescheck.click()

        botao_estado = self.driver.find_element_by_link_text("Santa Catarina")
        time.sleep(3)
        botao_estado.click()
        time.sleep(3)



        # print(f'{title} R$: {price}')

        botao_escolher_praia = self.driver.find_element_by_link_text(self.pergunta)
        time.sleep(3)
        botao_escolher_praia.click()
        time.sleep(2)
        self.driver.execute_script('window.scrollBy(0,800)')
        time.sleep(10)
        self.driver.execute_script('window.scrollBy(0,1200)')


curso = CursoAutomacao()
curso.Iniciar()