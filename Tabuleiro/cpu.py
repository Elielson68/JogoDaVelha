from .jogador import Jogador
from random import randint

class CPU(Jogador):
    def __init__(self, nome=None, simbolo=None):
        super().__init__(nome or "CPU", simbolo or "O")

    def getMovimentoCPU(self):
        movimento = randint(0, 8)
        return movimento
