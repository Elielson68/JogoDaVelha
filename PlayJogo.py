from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
from Tabuleiro.cpu import CPU
from Jogo.JogoController import JogarNovamente, MenuOpcoes
tabu = Tabuleiro()
jogador1 = Jogador("Player 1", "X")
jogador2 = Jogador("Player 2", "O")
CPU = CPU()

while True:
    MenuOpcoes()
    usuario = int(input("Você: "))
    if usuario==1:
        tabu.setJogadores(jogador1)
        tabu.setJogadores(jogador2)
        while True:
            print(tabu.MostrarTabuleiro())
            if tabu.isGanhador():
                tabu.setVez(tabu.RevezarVez())
                print("O ganhador é ", tabu.getNomeJogadorDaVez())
                usuario = JogarNovamente(tabu, jogador1, jogador2)
                if usuario:
                    continue
                if usuario == 2:
                    break
            if not tabu.isCasasDisponiveis():
                print("Não houve ganhadores! Empate!")
                usuario = JogarNovamente(tabu, jogador1, jogador2)
                if usuario:
                    continue
                if usuario == 2:
                    break
            print("Vez dê ", tabu.getNomeJogadorDaVez())
            jogada = input("Digite sua jogada: ")
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    elif usuario==2:
        tabu.setJogadores(jogador1)
        tabu.setJogadores(CPU)
        CPU.CarregarJogadas()
        CPU.SelecionarJogada()
        while True:
            print(tabu.MostrarTabuleiro())
            if tabu.isGanhador():
                tabu.setVez(tabu.RevezarVez())
                print("O ganhador é ", tabu.getNomeJogadorDaVez())
                if tabu.getNomeJogadorDaVez() == CPU.getNome():
                    if not CPU.isJogadaEmArquivo():
                        CPU.SalvarJogada()
                CPU.ResetarCPU()
                usuario = JogarNovamente(tabu, jogador1, CPU)
                if usuario == 1:
                    CPU.CarregarJogadas()
                    CPU.SelecionarJogada()
                    continue
                if usuario == 2:
                    break
            if not tabu.isCasasDisponiveis():
                print("Não houve ganhadores! Empate!")
                usuario = JogarNovamente(tabu, jogador1, CPU)
                CPU.ResetarCPU()
                if usuario == 1:
                    continue
                if usuario == 2:
                    break
            print("Vez dê ", tabu.getNomeJogadorDaVez())
            jogada = ""
            if tabu.getNomeJogadorDaVez() == jogador1.getNome():
                jogada = input("Digite sua jogada: ")
            else:
                jogada = CPU.ProximaJogada()
                print(jogada)
                if not tabu.isJogadaEstaNoDecodificador(jogada):
                    movimento_CPU = CPU.getMovimentoCPU()
                    jogada = tabu.getListKeysDecodificador()[movimento_CPU]
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    else:
        print("Adios!")
        break