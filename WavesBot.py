from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CursoAutomacao:
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument('--lang=pt-BR')
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)
		self.site = input("Qual o site você desenha navegar?")

	def Iniciar(self):
		self.driver.get(self.site)

curso = CursoAutomacao()
curso.Iniciar()		


