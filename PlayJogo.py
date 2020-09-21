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
                else:
                    if not CPU.isJogadaEmArquivo(jogador1.getMovimento()):
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
                if not tabu.isJogadaEstaNoDecodificador(jogada):
                    movimento_CPU = CPU.getMovimentoCPU()
                    jogada = tabu.getListKeysDecodificador()[movimento_CPU]
            tabu.setJogada(jogada)
        tabu.RemoverJogadores()
    elif usuario==3:
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
    else:
        print("Adios!")
        break