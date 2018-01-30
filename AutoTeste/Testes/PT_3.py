from .. import * 

class PT_3(Teste):

    def setUp(self):
        chrome(self)
  
    def teste_logar_email_incorreto(self):
        acessar(URL)
        verificar.titulo_da_pagina("Login")
        inserir_texto(campo_nome, "teste")
        inserir_texto(campo_email, "teste")
        inserir_texto(campo_senha, "123456")
        click(botao_logar)
        verificar.atributo_do_elemento(campo_email, "class", "validate invalid")
        inserir_texto(campo_email, "teste@")
        click(botao_logar)
        verificar.atributo_do_elemento(campo_email, "class", "validate invalid")
    
    def tearDown(self):
        fecharNavegador()