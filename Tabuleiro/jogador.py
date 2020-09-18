class Jogador():
    """
        Essa é uma classe para instanciar um objeto jogador.

    """
    def __init__(self, nome=None):
        self.nome = nome or "Player 1"
        self.movimentos = []
        self.tabela_potuacao = {"A1": 7, "A2": 8, "A3": 9,
                                "B1": 4, "B2": 5, "B3": 6,
                                "C1": 1, "C2": 2, "C3": 3
                              }
        self.pontuacao = 0
        self.simbolo = "X"

    def setMovimento(self, movimento: str) -> None:
        '''
        Acrescenta um movimento a lista de movimentos.
        :param movimento: String
        :return: None
        '''
        self.movimentos.append(movimento)

    def setPontuacao(self, ponto: int) -> None:
        '''
        Define a pontuação do objeto.
        :param ponto: Number int
        :return: None
        '''
        self.pontuacao += self.tabela_potuacao[ponto]

    def getPontuacao(self) -> int:
        '''
        Retorna a pontuação atual do objeto.
        :return: Number int
        '''
        return self.pontuacao

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