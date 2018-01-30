from Facilitador import *
from Dados import *


def logar():
    acessar(URL)
    verificar.titulo_da_pagina("Login")
    inserir_texto(campo_nome, "teste")
    inserir_texto(campo_email, "teste@teste")
    inserir_texto(campo_senha, "123456")
    click(botao_logar)
    aguardar.algum_elemento(5)
    verificar.titulo_da_pagina("Pagina 1")