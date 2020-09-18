from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
tabu = Tabuleiro()
jogador1 = Jogador("Player 1")
jogador2 = Jogador("Player 2")
jogador1.setSimbolo("X")
jogador2.setSimbolo("O")
tabu.setJogadores(jogador1)
tabu.setJogadores(jogador2)

while True:
    print(tabu.MostrarTabuleiro())
    if not tabu.isCasasDisponiveis():
        break
    if tabu.isGanhador():
        tabu.setVez(tabu.RevezarVez())
        print("O ganhador é ", tabu.getNomeJogadorDaVez())
        break
    print("Vez dê ", tabu.getNomeJogadorDaVez())
    jogada = input("Digite sua jogada: ")
    tabu.setJogada(jogada)