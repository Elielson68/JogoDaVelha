from .jogador import Jogador
from random import randint
import json

class CPU(Jogador):
    def __init__(self, nome=None, simbolo=None):
        super().__init__(nome or "CPU", simbolo or "O")
        self.arquivo_com_jogadas = None
        self.list_de_jogadas_futuras = []
        self.jogadas_futuras = None
        self.proxima_jogada = -1

    def getMovimentoCPU(self):
        movimento = randint(0, 8)
        return movimento

    def SalvarJogada(self):
        self.arquivo_com_jogadas = open("Tabuleiro/Jogadas_CPU/jogadas.txt", "a")
        jogadas_em_string = str(self.getMovimento())+'\n'
        self.arquivo_com_jogadas.write(jogadas_em_string)
        self.arquivo_com_jogadas.close()

    def CarregarJogadas(self):
        self.arquivo_com_jogadas = open("Tabuleiro/Jogadas_CPU/jogadas.txt", "r")
        self.list_de_jogadas_futuras = []
        for linha in self.arquivo_com_jogadas:
            self.list_de_jogadas_futuras.append(eval(linha))
        self.arquivo_com_jogadas.close()

    def SelecionarJogada(self):
        tamanho_lista_jogadas = len(self.list_de_jogadas_futuras) - 1
        selecionar_jogada = randint(0, tamanho_lista_jogadas)
        self.jogadas_futuras = self.list_de_jogadas_futuras[selecionar_jogada]

    def ProximaJogada(self):
        if not self.isLimiteJogadasFuturas(self.proxima_jogada):
            self.proxima_jogada += 1
        return self.jogadas_futuras[self.proxima_jogada]

    def isLimiteJogadasFuturas(self, valor):
        if valor > len(self.jogadas_futuras)-1:
            return True
        else:
            return False
    def isJogadaEmArquivo(self):
        return self.movimentos in self.list_de_jogadas_futuras

    def ResetarCPU(self):
        self.arquivo_com_jogadas = None
        self.list_de_jogadas_futuras = []
        self.jogadas_futuras = None
        self.proxima_jogada = -1