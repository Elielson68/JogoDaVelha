class Jogador():
    """
        Essa é uma classe para instanciar um objeto jogador.

    """

    def __init__(self, nome=None, simbolo=None):
        self.nome = nome or "Player 1"
        self.movimentos = []
        self.simbolo = simbolo or "X"

    def setMovimento(self, movimento: str) -> None:
        '''
        Acrescenta um movimento a lista de movimentos.
        :param movimento: String
        :return: None
        '''
        self.movimentos.append(movimento)

    def getMovimento(self) -> list:
        '''
        Retorna a lista de movimentos do objeto.
        :return: List
        '''
        return self.movimentos

    def setNome(self, nome: str) -> None:
        '''
        Define o nome do objeto.
        :param nome: String
        :return: None
        '''
        self.nome = nome

    def getNome(self) -> str:
        '''
        Retorna o nome do objeto.
        :return: String
        '''
        return self.nome

    def setSimbolo(self, simbolo: str) -> None:
        '''
        Define o atributo símbolo do objeto criado
        :param simbolo: String
        :return: None
        '''
        self.simbolo = simbolo

    def getSimbolo(self) -> str:
        '''
        Retorna o símbolo do player atual.
        :return: String
        '''
        return self.simbolo

    def ResetarMovimentos(self) -> None:
        '''
        Reseta a lista de movimentos realizados
        :return: None
        '''
        self.movimentos = []