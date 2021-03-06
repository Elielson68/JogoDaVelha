from .jogador import Jogador
class Tabuleiro():
    """
            Essa é uma classe para instanciar o tabuleiro.
    """
    def __init__(self):
        self.casas = [["[-]"] * 3, ["[-]"] * 3, ["[-]"] * 3]
        self.decodificador = {
                              "A1": [0, 0], "A2": [0, 1], "A3": [0, 2],
                              "B1": [1, 0], "B2": [1, 1], "B3": [1, 2],
                              "C1": [2, 0], "C2": [2, 1], "C3": [2, 2]
                              }
        self.vez = 0
        self.jogadores = []
        self.sequencia_vitorias = [
                                   ["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
                                   ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"],
                                   ["A1", "B2", "C3"], ["C1", "B2", "A3"]
                                  ]

    def getCasas(self) -> list:
        '''
        Retorna a lista de casas do tabuleiro
        :return: List
        '''
        return self.casas

    def getListKeysDecodificador(self) -> list:
        '''
        Retorna uma lista com as chaves do decodificador.
        :return: List
        '''
        return list(self.decodificador.keys())

    def setJogada(self, jogada: str) -> None:
        '''
        Insere uma jogada no tabuleiro caso a jogada seja válida.
        Insere a jogada realizada na lista de jogadas do jogador atual.
        Reveza a vez do jogador atual.
        :param jogada: String
        :return: None
        '''
        if self.isJogadaValida(jogada) and self.isJogadaEstaNoDecodificador(jogada):
            linha = self.decodificador[jogada][0]
            coluna = self.decodificador[jogada][1]
            self.casas[linha][coluna] = "["+self.jogadores[self.vez].getSimbolo()+"]"
            self.jogadores[self.vez].setMovimento(jogada)
            nova_vez = self.RevezarVez()
            self.setVez(nova_vez)

    def isJogadaValida(self, jogada: str) -> bool:
        '''
        Retorna se a jogada realizada é válida ou não.
        :param jogada: String
        :return: Bool
        '''
        if (jogada in self.jogadores[0].getMovimento()) or (jogada in self.jogadores[1].getMovimento()):
            return False
        else:
            return True

    def isJogadaEstaNoDecodificador(self, jogada: str) -> bool:
        '''
        Retorna se a jogada feita está dentro do decodificador
        :param jogada: Sring
        :return: Bool
        '''
        return jogada in self.decodificador

    def setJogadores(self, jogador: Jogador) -> None:
        '''
        Insere um jogador na lista de jogadores caso ainda haja espaço.
        :param jogador: Jogador
        :return: None
        '''
        if not self.isLimiteJogadores():
            self.jogadores.append(jogador)

    def getJogadores(self) -> list:
        '''
        Retorna a lista de jogadores.
        :return: List
        '''
        return self.jogadores

    def setVez(self, vez: int) -> None:
        '''
        Define a vez de quem deve jogar.
        :param vez: int
        :return: None
        '''
        self.vez = vez

    def getVez(self) -> int:
        '''
        Retorna de quem é a vez.
        :return: Number int
        '''
        return self.vez

    def getNomeJogadorDaVez(self) -> str:
        '''
        Retorna o nome do jogador da vez.
        :return: String
        '''
        return self.jogadores[self.vez].getNome()

    def isLimiteJogadores(self) -> bool:
        '''
        Retorna  verdadeiro se o limite de jogadores excedeu o máximo permitido.
        :return: Bool
        '''
        total_jogadores = len(self.jogadores)
        if total_jogadores > 1:
            return True
        else:
            return False

    def MostrarTabuleiro(self) -> str:
        '''
        Formata o tabuleiro e retorna ele em forma de string.
        :return: String
        '''
        tabuleiro_formatado = "\t 1\t 2\t 3\n"
        casas = ["A: \t", "B: \t", "C: \t"]
        i = 0
        for x in self.casas:
            tabuleiro_formatado += casas[i]
            i += 1
            for y in x:
                tabuleiro_formatado += y+"\t"
            tabuleiro_formatado += "\n"
        return tabuleiro_formatado

    def isCasasDisponiveis(self) -> bool:
        '''
        Retorna verdadeiro caso hajam casas disponíveis.
        :return: Bool
        '''
        CasasMarcadas = len(self.jogadores[0].getMovimento()) + len(self.jogadores[1].getMovimento())
        if CasasMarcadas == 9:
            return False
        else:
            return True

    def isGanhador(self) -> bool:
        '''
        Retorna verdadeiro caso o jogador da última rodada tenha ganhado fazendo algumas das sequências de vitória.
        :return: Bool
        '''
        vez_do_jogador_anterior = self.RevezarVez()
        for sequencia_de_movimentos_para_vitoria in self.sequencia_vitorias:
            lista_de_movimentos = [movimento for movimento in self.jogadores[vez_do_jogador_anterior].getMovimento() if movimento in sequencia_de_movimentos_para_vitoria]
            if len(lista_de_movimentos) == 3:
                return True
        return False

    def RevezarVez(self) -> int:
        '''
        Retorna a vez do próximo jogador.
        :return: Number int
        '''
        return 0 if self.getVez() else 1

    def ResetarCasas(self) -> None:
        '''
        Reseta as casas pro valor padrão inicial
        :return: None
        '''
        self.casas = [["[-]"] * 3, ["[-]"] * 3, ["[-]"] * 3]

    def RemoverJogadores(self) -> None:
        '''
        Remove todos os jogadores
        :return: None
        '''
        self.jogadores = []
