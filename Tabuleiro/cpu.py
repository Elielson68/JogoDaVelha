from .jogador import Jogador
from random import randint

class CPU(Jogador):
    def __init__(self, nome=None, simbolo=None):
        super().__init__(nome or "CPU", simbolo or "O")
        self.arquivo_com_jogadas = None
        self.list_de_jogadas_futuras = []
        self.jogadas_futuras = []
        self.proxima_jogada = -1

    def getMovimentoCPU(self) -> int:
        '''
        Retorna um número inteiro entre 0 e 8, equivalente ao número de casas do tabuleiro
        :return: Number int
        '''
        return randint(0, 8)

    def SalvarJogada(self, movimento=None) -> None:
        '''
        Retorna None
        Salva as jogadas realizadas pela CPU em um arquivo chamado jogadas.txt
        :return:
        '''
        self.arquivo_com_jogadas = open("Tabuleiro/Jogadas_CPU/jogadas.txt", "a")
        jogadas_em_string = str(movimento or self.getMovimento())+'\n'
        self.arquivo_com_jogadas.write(jogadas_em_string)
        self.arquivo_com_jogadas.close()

    def CarregarJogadas(self) -> None:
        '''
        Retorna None.
        Carrega a lista de jogadas armazenadas no arquivo jogadas.txt no atributo self.list_de_jogadas_futuras
        :return: None
        '''
        self.arquivo_com_jogadas = open("Tabuleiro/Jogadas_CPU/jogadas.txt", "r")
        self.list_de_jogadas_futuras = []
        for linha in self.arquivo_com_jogadas:
            if linha:
                self.list_de_jogadas_futuras.append(eval(linha))
        self.arquivo_com_jogadas.close()

    def SelecionarJogada(self) -> None:
        '''
        Verifica se a lista de jogadas possui alguma jogada
        Então é selecionada aleatoriamente alguma jogada da lista de jogadas
        :return: None
        '''
        tamanho_lista_jogadas = len(self.list_de_jogadas_futuras) - 1
        if tamanho_lista_jogadas >= 0:
            selecionar_jogada = randint(0, tamanho_lista_jogadas)
            self.jogadas_futuras = self.list_de_jogadas_futuras[selecionar_jogada]

    def ProximaJogada(self) -> None:
        '''
        Verifica se a próxima jogada a ser feita está dentro do limite da lista de jogadas atual
        Verifica se a lista JogadasFuturas possui alguma jogada nela
        Caso as duas condições sejam verdadeiras, o programa insere +1 no atributo proxima_jogada e então retorna a próxima jogada a ser feita pela CPU
        :return: None
        '''
        jogada = ""
        if not self.isLimiteJogadasFuturas(self.proxima_jogada+1) and self.isValorEmJogadasFuturas():
            self.proxima_jogada += 1
            jogada = self.jogadas_futuras[self.proxima_jogada]
        return jogada

    def isLimiteJogadasFuturas(self, valor: int) -> bool:
        '''
        Verifica se o valor inserido está dentro do limite de valores da lista de jogadas_futuras
        :param valor: Number int
        :return: Bool
        '''
        if valor > len(self.jogadas_futuras)-1:
            return True
        else:
            return False

    def isValorEmJogadasFuturas(self) -> None:
        '''
        Verifica se há algum valor dentro do atributo jogadas_futuras
        :return: None
        '''
        if len(self.jogadas_futuras) > 0:
            return True
        else:
            return False

    def isJogadaEmArquivo(self, movimento=None) -> None:
        '''
        Verifica se a jogada atual já está inserida no atributo list_de_jogadas_futuras
        :return: None
        '''
        movimento_ganhador = movimento or self.movimentos
        return movimento_ganhador in self.list_de_jogadas_futuras

    def ResetarCPU(self) -> None:
        '''
        Reseta todos os atributos da CPU
        :return: None
        '''
        self.arquivo_com_jogadas = None
        self.list_de_jogadas_futuras = []
        self.jogadas_futuras = []
        self.proxima_jogada = -1