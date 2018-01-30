from .. import * 

class PT_2(Teste):

    def setUp(self):
        chrome(self)

    def teste_logar_com_sucesso(self):
        acessar(URL)
        verificar.titulo_da_pagina("Login")
        inserir_texto(campo_nome, "teste")
        inserir_texto(campo_email, "teste@teste")
        inserir_texto(campo_senha, "123456")
        click(botao_logar)
        aguardar.algum_elemento(5)
        verificar.titulo_da_pagina("Pagina 1")
  
    def tearDown(self):
        fecharNavegador()