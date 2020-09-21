from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
from Tabuleiro.cpu import CPU
from Jogo.JogoController import JogarNovamente, MenuOpcoes
tabu = Tabuleiro()
jogador1 = Jogador("Player 1", "X")
jogador2 = Jogador("Player 2", "O")
CPU2 = CPU(nome="CPU 2",simbolo="X")
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
                if usuario == 1:
                    continue
                elif usuario == 2:
                    break
                else:
                    break
            if not tabu.isCasasDisponiveis():
                print("Não houve ganhadores! Empate!")
                usuario = JogarNovamente(tabu, jogador1, jogador2)
                if usuario == 1:
                    continue
                elif usuario == 2:
                    break
                else:
                    break
            print("Vez dê ", tabu.getNomeJogadorDaVez())
            jogada = input("Digite sua jogada: ")
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    elif usuario == 2:
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
                    CPU.SalvarJogada()
                else:
                    CPU.SalvarJogada(jogador1.getMovimento())
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
                elif usuario == 2:
                    break
                else:
                    break
            print("Vez dê ", tabu.getNomeJogadorDaVez())
            jogada = ""
            if tabu.getNomeJogadorDaVez() == jogador1.getNome():
                jogada = input("Digite sua jogada: ")
            else:
                jogada = CPU.ProximaJogada()
                print(jogada)
                if not tabu.isJogadaEstaNoDecodificador(jogada):
                    print("Entrou")
                    movimento_CPU = CPU.getMovimentoCPU()
                    jogada = tabu.getListKeysDecodificador()[movimento_CPU]
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    elif usuario == 3:
        while True:
            print("Escolha uma das opções para personalizar o que deseja:\n1 - Personalizar Nome dos players\n2 - Personalizar Símbolo dos players\n3 - Voltar ao menu principal")
            usuario = int(input("Você: "))
            if usuario==1:
                opcao = int(input("1 - Personalizar o nome do Player 1\n2 - Personalizar o nome do Player 2\n3 - Personalizar o nome da CPU\n4 - Sair\nVocê: "))
                novo_nome = input("Digite o novo nome: ")
                if opcao == 1:
                    jogador1.setNome(novo_nome)
                elif opcao == 2:
                    jogador2.setNome(novo_nome)
                elif opcao == 3:
                    CPU.setNome(novo_nome)
                else:
                    break
                print("Nome alterado com sucesso!\n")
            elif usuario == 2:
                opcao = int(input("1 - Personalizar o símbolo do Player 1\n2 - Personalizar o símbolo do Player 2\n3 - Personalizar o símbolo da CPU\n4 - Sair\nVocê: "))
                novo_simbolo = input("Digite o novo símbolo: ")
                if opcao == 1:
                    jogador1.setSimbolo(novo_simbolo)
                elif opcao == 2:
                    jogador2.setSimbolo(novo_simbolo)
                elif opcao == 3:
                    CPU.setSimbolo(novo_simbolo)
                else:
                    break
                print("Símbolo alterado com sucesso!\n")
            else:
                break
    elif usuario == 4:
        tabu.setJogadores(CPU2)
        tabu.setJogadores(CPU)
        CPU.CarregarJogadas()
        CPU.SelecionarJogada()
        CPU2.CarregarJogadas()
        CPU2.SelecionarJogada()
        while True:
            print(tabu.MostrarTabuleiro())
            if tabu.isGanhador():
                tabu.setVez(tabu.RevezarVez())
                print("O ganhador é ", tabu.getNomeJogadorDaVez())
                if tabu.getNomeJogadorDaVez() == CPU.getNome():
                    CPU.SalvarJogada()
                else:
                    CPU2.SalvarJogada()
                CPU.ResetarCPU()
                CPU2.ResetarCPU()
                usuario = JogarNovamente(tabu, CPU2, CPU)
                if usuario == 1:
                    CPU.CarregarJogadas()
                    CPU.SelecionarJogada()
                    CPU2.CarregarJogadas()
                    CPU2.SelecionarJogada()
                    continue
                if usuario == 2:
                    break
            if not tabu.isCasasDisponiveis():
                print("Não houve ganhadores! Empate!")
                usuario = JogarNovamente(tabu, CPU2, CPU)
                CPU.ResetarCPU()
                CPU2.ResetarCPU()
                if usuario == 1:
                    continue
                elif usuario == 2:
                    break
                else:
                    break
            print("Vez dê ", tabu.getNomeJogadorDaVez())
            jogada = ""
            if tabu.getNomeJogadorDaVez() == CPU2.getNome():
                jogada = CPU.ProximaJogada()
                print(jogada)
                if not tabu.isJogadaEstaNoDecodificador(jogada):
                    print("cpu 2")
                    movimento_CPU = CPU.getMovimentoCPU()
                    jogada = tabu.getListKeysDecodificador()[movimento_CPU]
            else:
                jogada = CPU.ProximaJogada()
                print(jogada)
                if not tabu.isJogadaEstaNoDecodificador(jogada):
                    print("cpu 1")
                    movimento_CPU = CPU.getMovimentoCPU()
                    jogada = tabu.getListKeysDecodificador()[movimento_CPU]
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    else:
        print("Adios!")
        break