import unittest
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# utilizado no aguarde do elemento
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# eventos com ações do mouse e outros eventos
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

controleExterno = None
navegador = None
Teste = unittest.TestCase

class Verificacao(object):
    """Classe utilizada para realizar as verificacoes do teste"""
    def titulo_da_pagina(self, titulo):
        """Função que compara o titulo da página do navegador com o titulo enviado."""
        global navegador, controleExterno
        controleExterno.assertIn(titulo, navegador.title)
    
    def conteudo_da_pagina(self, texto):
        """Função para buscar um texto no código fonte da página web. """
        global navegador
        try:
            assert texto in navegador.page_source
        except:
            controleExterno.fail("Texto \""+texto+"\" não foi localizado na pagina web.")
            pass
    
    def atributo_do_elemento(self, campo, atributo, valor):
        global navegador, controleExterno
        try:
            element = elemento(campo.tipo, campo.dado)
            valor_atributo = element.get_attribute(atributo)
            controleExterno.assertIn(valor_atributo, valor)
        except:
            controleExterno.fail("Falha ao comparar a/o \""+atributo+"\" \""+valor+"\" com os dados do elemento.")
            pass
    
    def texto_do_elemento(self, campo, texto):
        """Função para comparar o texto do elemento. """
        global navegador
        try:
            element = elemento(campo.tipo, campo.dado)
            controleExterno.assertIn(element.text, texto)
        except:
            controleExterno.fail("O texto \""+texto+"\" é diferente do texto do elemento da pagina.")
            pass
    
    def opcao_selecionada(self, campo, texto):
        """Função para comparar o texto da opção selecionada."""
        global navegador
        try:
            element = elemento(campo.tipo, campo.dado)
            select = Select(element)
            selected_option = select.first_selected_option
            controleExterno.assertIn(selected_option.text, texto)
        except:
            controleExterno.fail("O texto \""+texto+"\" é diferente da opção selecionada no campo.")
            pass

verificar = Verificacao()

class Aguardar(object):
    def exatamente(self, segundos):
        """Função que faz com que o sistema aguarde um tempo exato para prosseguir. Normalmente não é indicada pois pode desperdiçar tempo de teste, ao contrário da função *algum_elemento(segundos)*."""
        time.sleep(segundos)
    
    def algum_elemento(self, segundos):
        """Função destinada a aguardar a aparição de qualquer elemento que não esteja disponível imediatamente (medido em segundos)."""
        global navegador
        navegador.implicitly_wait(segundos)
    
    def elemento_aparecer(self, campo, segundos):
        """Função que aguardará a aparição de algum elemento específico, por determinado tempo."""
        global navegador, controleExterno
        try:
            element = WebDriverWait(navegador, segundos).until(
                EC.presence_of_element_located((campo.tipo, campo.dado))
            )
        except:
            controleExterno.fail("Falha ao tentar localizar o elemento \"" + campo.dado +"\ do tipo \"" + campo.tipo + "\"")
            pass
        
        # menu = elemento(tipoCampo, valor)
        # actions = ActionChains(navegador)
        # actions.move_to_element(menu)
        # actions.click(menu)
        # actions.perform()

aguardar = Aguardar()

class Pressionar(object):
    """Classe utilizada para pressionar alguma tecla"""
    def enter(self, campo):
        """Função que pressiona a tecla ENTER sobre algum campo da pagina web"""
        global navegador, controleExterno
        element = elemento(campo.tipo, campo.dado)
        element.send_keys(Keys.ENTER)
    
    def retornar(self, campo):
        """Função que pressiona a tecla RETURN sobre algum campo da pagina web"""
        global navegador, controleExterno
        element = elemento(campo.tipo, campo.dado)
        element.send_keys(Keys.RETURN)
    
    def tab(self, campo):
        """Função que pressiona a tecla TAB sobre algum campo da pagina web"""
        global navegador, controleExterno
        element = elemento(campo.tipo, campo.dado)
        element.send_keys(Keys.TAB)
    
    def seta_baixo(self, campo):
        """Função que pressiona a seta para baixo sobre algum campo da pagina web"""
        global navegador, controleExterno
        element = elemento(campo.tipo, campo.dado)
        element.send_keys(Keys.ARROW_DOWN)
    
    def seta_cima(self, campo):
        """Função que pressiona a seta para cima sobre algum campo da pagina web"""
        global navegador, controleExterno
        element = elemento(campo.tipo, campo.dado)
        element.send_keys(Keys.ARROW_UP)
    
pressionar = Pressionar()

def acessar(link):
    """Função para abrir alguma página no navegador utilizado no teste"""
    navegador.get(link)

def fecharNavegador():
    """Função para fechar o navegador e finalizar o teste"""
    navegador.close()

# Outras funções
def hoje():
    """Função que retorna a data de hoje, no formato(DD/MM/AAAA)"""
    now = datetime.now()
    return str(now.day) + '/' + str(now.month) + '/' + str(now.year)

# Começar unittest
def iniciarTeste():
    """Função que chama o método Main da classe *unittest*"""
    unittest.main()

# Navegadores
def chrome(controle):
    """Função que permite receber uma instancia de uma janela do Chrome"""
    global navegador, controleExterno
    controleExterno = controle
    driver = webdriver.Chrome()
    navegador = driver
    return driver

def firefox(controle):
    """Função que permite receber uma instancia de uma janela do Firefox"""
    global navegador, controleExterno
    controleExterno = controle
    driver = webdriver.Firefox()
    navegador = driver
    return driver

# verifica se o elemento existe e retornar o elemento
def elemento(tipoCampo, valor):
    """Função para receber um elemento da página web."""
    global navegador, controleExterno
    try:
        return navegador.find_element(tipoCampo, valor)
    except NoSuchElementException:
        controleExterno.fail("Falha ao tentar localizar o elemento \"" + valor +"\ do tipo \"" + tipoCampo + "\"")
        pass
    return None

# verifica se o elemento existe e retornar uma lista caso exista
def elementos(tipoCampo, valor):
    """Função para receber uma lista de elementos da página web."""
    global navegador, controleExterno
    try:
        return navegador.find_elements(tipoCampo, valor)
    except NoSuchElementException:
        controleExterno.fail("Falha ao tentar localizar algum elemento \"" + valor +"\ do tipo \"" + tipoCampo + "\"")
        pass
    return None

#Limpa o campo, insere o texto e tecla ENTER
def inserir_texto(campo, texto):   
    """Função para inserir texto em algum campo ou elemento da página web."""
    element = elemento(campo.tipo, campo.dado)
    element.clear()
    element.send_keys(texto)
    # element.send_keys(Keys.RETURN)

def click(campo):
    """Função para clicar sobre algum elemento da página web."""
    element = elemento(campo.tipo, campo.dado)
    element.click()

def click(campo):
    """Função para clicar sobre algum elemento da página web."""
    element = elemento(campo.tipo, campo.dado)
    element.click()
    