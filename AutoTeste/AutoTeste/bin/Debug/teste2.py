from Funcao import *
import sys

class TesteLogin(Teste):

    def setUp(self):
        chrome(self)

    def teste_logar_com_sucesso(self):
        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_texto(campo_usuario, "francisco_faria@inatel.br")
        inserir_textos(campo_senha, "123456", 2)
        click(botao_logar)
        aguardar.algum_elemento(5)
        verificar.titulo_da_pagina("SLPF")
        verificar.conteudo_da_pagina("Monitoramento Geral")
    
    def teste_logar_com_usuario_invalido(self):
        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_texto(campo_usuario, "usuario_sem_cadastro@inatel.br")
        inserir_textos(campo_senha, "123456", 2)
        click(botao_logar)
        verificar.conteudo_da_pagina("Usuário ou senha inválidos.")

    def teste_logar_sem_inserir_senha(self):
        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_texto(campo_usuario, "francisco_faria@inatel.br")
        verificar.esta_desabilitado(botao_logar)
    
    def teste_logar_sem_inserir_login(self):
        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_textos(campo_senha, "123456", 2)
        verificar.esta_desabilitado(botao_logar)

    def teste_logar_campos_vazios(self):
        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        verificar.esta_desabilitado(botao_logar)
    
    def teste_logar_email_invalido(self):

        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_textos(campo_senha, "123456", 2)

        inserir_texto(campo_usuario, "email1")
        verificar.conteudo_da_pagina("O Login deve conter pelo menos 8 caracteres")
        verificar.esta_desabilitado(botao_logar)

        inserir_texto(campo_usuario, "email1@uol")
        verificar.conteudo_da_pagina("Login inválido")
        verificar.esta_desabilitado(botao_logar)

        inserir_texto(campo_usuario, "email1@uol.")
        verificar.conteudo_da_pagina("Login inválido")
        verificar.esta_desabilitado(botao_logar)

    def teste_logar_limite_de_caracteres_dos_campos(self):

        acessar(URL)
        verificar.titulo_da_pagina("SLPF")
        inserir_textos(campo_senha, "123456", 2)
        valor_campo = ""

        inserir_texto(campo_usuario, "123456789012345678901234567890123456789012345678901234567890ABC")
        valor_campo = verificar.valor_do_campo(campo_usuario)
        verificar.sao_iguais(valor_campo, "123456789012345678901234567890123456789012345678901234567890")

        inserir_textos(campo_senha, "123", 2)
        verificar.conteudo_da_pagina("A senha deve conter pelo menos 6 caracteres")
        verificar.esta_desabilitado(botao_logar)

        inserir_textos(campo_senha, "123456", 2)
        inserir_texto(campo_usuario, "email1@uol.")
        verificar.conteudo_da_pagina("Login inválido")
        verificar.esta_desabilitado(botao_logar)
        
    def tearDown(self):
        fecharNavegador()

def suite_de_testes():
    """Suite de todos os testes que iniciam com a palavra teste"""
    return unittest.makeSuite( TesteLogin, 'teste' )

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_de_testes())
    #print("Digite algo para sair: ")
    #sys.stdin.readline()