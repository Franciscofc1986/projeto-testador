class Tipo(object):
    """
    Tipos de dados aceito nas tags.
    """
    ID = "id"
    XPATH = "xpath"
    LINK = "link text"
    PARTE_LINK = "partial link text"
    NOME = "name"
    NOME_TAG = "tag name"
    CLASSE = "class name"
    CSS = "css selector"

class dado(object):
    def __init__(self, tipo, _dado):
        self.tipo = tipo
        self.dado = _dado