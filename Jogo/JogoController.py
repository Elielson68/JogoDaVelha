from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador

def MenuOpcoes():
    print("\t\tJOGO DA VELHA\n")
    print("1 - Jogar contra outro Player")
    print("2 - Jogar contra CPU")
    print("3 - Sair")

def JogarNovamente(tabuleiro: Tabuleiro, jogador1: Jogador, jogador2: Jogador)->int:
    '''
    Retorna 1 caso o jogador desejar jogar novamente, retorna 0 caso não.
    :return: Number int
    '''
    usuario = int(input("Deseja jogar novamente?\n1 - Sim\n2 - Não\nVocê: "))
    jogador1.ResetarMovimentos()
    jogador2.ResetarMovimentos()
    tabuleiro.ResetarCasas()
    tabuleiro.setVez(0)
    return usuario