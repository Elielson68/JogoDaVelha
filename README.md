# JogoDaVelha
Este é um pacote de jogo da velha desenvolvido em python utilizando conceitos de orientação a objetos.

# Sumário

1. [INSTALAÇÃO](#1-instalao)

    1.1. [Como baixar o jogo em pacote via pip](#11-como-baixar-o-jogo-em-pacote-via-pip)
    
    1.2. [Como baixar/clonar o projeto completo do github](#12-como-baixarclonar-o-projeto-completo-do-github)

2. [CRIANDO SEU JOGO](#2-criando-seu-jogo)

    2.1. [Jogador vs Jogador](#21-jogador-vs-jogador)
        
    2.2. [Jogador vs CPU](#22-jogador-vs-cpu)
    
    2.3. [CPU vs CPU](#23-cpu-vs-cpu-)

3. [RODANDO JOGO PRONTO](#3-rodando-jogo-pronto)

# 1. INSTALAÇÃO

## 1.1. Como baixar o jogo em pacote via pip.
Para instalar a biblioteca via gerenciador de pacotes basta rodar o comando abaixo em seu terminal:

    pip install JogoDaVelha-Elielson68
   
E então a biblioteca principal estará disponível para você montar seu jogo a seu estilo.
Abaixo em  <b>Criando seu jogo</b> há mais explicações sobre.

## 1.2. Como baixar/clonar o projeto completo do github.

Caso deseje clonar o projeto todo com um jogo pronto incluso, rode o comando:

    git clone https://github.com/Elielson68/JogoDaVelha.git
   
Para baixar o arquivo .zip basta acessar <a href="https://github.com/Elielson68/JogoDaVelha/archive/master.zip">https://github.com/Elielson68/JogoDaVelha/archive/master.zip</a>.

# 2 CRIANDO SEU JOGO

Esta biblioteca permite você criar o jogo para ser jogado tanto jogador vs jogador, jogador vs CPU e também CPU vs CPU. Abaixo os passos a passos de como criar cada tipo de jogo.

## 2.1. Jogador vs Jogador

Caso você tenha instalado o pacote via gerenciador de pacotes pode iniciar direto do passo abaixo. Caso tenha baixado ou clonado, antes de iniciar o passo abaixo você deve criar um arquivo .py na pasta JogoDaVelha e então pode continuar seguindo os passos indicados.

### 2.1.1. Criando objetos.

Primeiro importe o pacote tabuleiro e jogador para seu arquivo python.

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
```

Feitas as importações você pode criar os objetos Tabuleiro e Jogador.

```python
tabuleiro_velha = Tabuleiro()
jogador_1 = Jogador("Player 1", "X")
jogador_2 = Jogador("Player 2", "O")
```  

Você pode substituir os valores "Player 1" e "Player 2" por outro valor que achar ser mais adequado. O mesmo equivale para os símbolos "X" e "O".

### 2.1.2. Inserindo jogadores no tabuleiro.

Após ter criado os jogadores, agora você deve inserir os mesmos no tabuleiro.

Para isso utilize o método <b>setJogadores()</b>

```python
tabuleiro_velha.setJogadores(jogador_1)
tabuleiro_velha.setJogadores(jogador_2)
```

## 2.1.3. Mostrando o tabuleiro.

Para mostrar o tabuleiro basta chamar o método <b>MostrarTabuleiro()</b> do nosso objeto tabuleiro_velha.

```python
print(tabuleiro_velha.MostrarTabuleiro())
``` 

Aparecerá algo deste tipo:

             1       2       3
    A: 	[-]	[-]	[-]	
    B: 	[-]	[-]	[-]	
    C: 	[-]	[-]	[-]	

## 2.1.4. Realizando jogadas.

Com os jogadores no tabuleiro e com o tabuleiro sendo impresso, agora basta fazer a jogada.

Para fazer uma jogada basta indicar a linha, que são representadas pelas letras A, B e C. E logo em seguida indicar a coluna, representadas pelos números: 1,2 e 3.

Usamos o método <b>setJogada()</b> do nosso objeto tabuleiro_velha para isso.

```python
tabuleiro_velha.setJogada("A1")
```

O resultado se imprimirmos o tabuleiro novamente será algo deste tipo:

```python
print(tabuleiro_velha.MostrarTabuleiro())
```
  
     	 1	 2	 3
    A: 	[X]	[-]	[-]	
    B: 	[-]	[-]	[-]	
    C: 	[-]	[-]	[-]
    
## 2.1.5. Mostrando a vez de quem deve jogar.

A cada jogada realizada o tabuleiro irá revezar de jogador_1 para jogador_2. Se for de seu agrado mostrar de quem é a vez basta utlizar o método <b>getNomeJogadorDaVez()</b>

```python
print(tabuleiro_velha.getNomeJogadorDaVez())
```
    
## 2.1.6. Vericando vitória de jogador.

A cada jogada realizada é possível verificar se houve algum ganhador. Para realizar a verificação basta utilizar o método <b>isGanhador()</b> que retorna se a última jogada realizada resultou na vitória do jogador da vez passada.

```python
print(tabuleiro_velha.isGanhador())
```

## 2.1.7. Verificando se há casas disponíveis.

Para verificar se ainda há casas disponíveis para jogar basta utilizar o método <b>isCasasDisponiveis()</b> que retorna 'True' se há casas disponíveis e 'False' se não há.

```python
print(tabuleiro_velha.isCasasDisponiveis())
```

## 2.1.8. Definindo a vez de quem começa.

Você pode escolher a vez de quem começa, por padrão o jogo sempre irá começar pelo primeiro jogador inserido no tabuleiro, para trocar quem inicia basta utilizar dois métodos que são <b>setVez()</b> e <b>RevezarVez()</b>.

```python
tabuleiro_velha.setVez(RevezarVez())
```

## 2.1.9. Código de jogo simples

Abaixo um código simples utilizando os passos anteriores.

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
tabuleiro_velha = Tabuleiro()
jogador_1 = Jogador("Player 1", "X")
jogador_2 = Jogador("Player 2", "O")
tabuleiro_velha.setJogadores(jogador_1)
tabuleiro_velha.setJogadores(jogador_2)
while True: 
    print(tabuleiro_velha.MostrarTabuleiro())
    if tabuleiro_velha.isGanhador(): #A cada jogada realizada será verificado se houve um ganhador
        tabuleiro_velha.setVez(tabuleiro_velha.RevezarVez()) #Como o ganhador foi o último jogador, então é necessário revezar a vez para o último jogador.
        print("O ganhador é ", tabuleiro_velha.getNomeJogadorDaVez())
        break
    if not tabuleiro_velha.isCasasDisponiveis(): #Se ninguém tiver ganho, então é verificado se o tabuleiro ainda possui casas disponíveis.
        print("Não houve ganhadores! Empate!")
        break
    print("Vez dê ", tabuleiro_velha.getNomeJogadorDaVez())
        jogada = input("Digite sua jogada: ")
        tabuleiro_velha.setJogada(jogada)
```

## 2.2. Jogador vs CPU

Os passos para desenvolver jogador vs CPU são os mesmos que para jogador vs jogador, as únicas diferenças são apenas na hora de inserir os jogadores no tabuleiro e de inserir jogadas.

### 2.2.1. Inserindo jogador e CPU no tabuleiro

Como agora você deve inserir uma CPU ao invés do jogador_2, você deve importar a classe CPU do pacote Tabuleiro e então criar o objeto CPU e então inserir no tabuleiro_velha para isso utilize o código abaixo:

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
from Tabuleiro.cpu import CPU
tabuleiro_velha = Tabuleiro()
jogador_1 = Jogador("Player 1", "X")
CPU = CPU()
tabuleiro_velha.setJogadores(jogador_1)
tabuleiro_velha.setJogadores(CPU)
```

### 2.2.2. Verificando a vez de quem deve jogar

Agora iremos verificar se a vez de quem deve jogar é do jogador_1 ou da CPU. Para isso utilizaremos uma condição simples em que ela verificará se o nome de quem tá jogando é do jogador_1 ou da CPU. Caso seja do jogador_1 então o programa pedirá para ele inserir sua jogada, caso seja da CPU a jogada será aleatória.

Para verificarmos o nome de quem está jogando, utilizaremos o método <b>getNomeJogadorDaVez()</b> do objeto tabuleiro_velha.

```python
jogada = ""
if tabuleiro_velha.getNomeJogadorDaVez() == jogador_1.getNome():
    jogada = input("Digite sua jogada: ")
```

### 2.2.3. Gerando jogada da CPU

A CPU possui o método <b>getMovimentoCPU()</b> que retorna um número aleatório de 0 a 8, representando os 9 valores possíveis no tabuleiro. O tabuleiro possui o método <b>getListKeysDecodificador()</b> que retorna uma lista com todas as casas no formato: "A1", "A2" etc. Desta forma, para obter a jogada da CPU teremos o código abaixo:

```python
jogada = ""
if tabuleiro_velha.getNomeJogadorDaVez() == jogador_1.getNome():
    jogada = input("Digite sua jogada: ")
else:
    movimento_CPU = CPU.getMovimentoCPU()
    jogada = tabuleiro_velha.getListKeysDecodificador()[movimento_CPU]
```

### 2.2.4. Código de Jogador vs CPU

Por fim, basta inserir essa última parte do jogo no código e teremos o resultado abaixo:

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.jogador import Jogador
from Tabuleiro.cpu import CPU
tabuleiro_velha = Tabuleiro()
jogador_1 = Jogador("Player 1", "X")
CPU = CPU()
tabuleiro_velha.setJogadores(jogador_1)
tabuleiro_velha.setJogadores(CPU)

while True: 
    print(tabuleiro_velha.MostrarTabuleiro())
    if tabuleiro_velha.isGanhador(): #A cada jogada realizada será verificado se houve um ganhador
        tabuleiro_velha.setVez(tabuleiro_velha.RevezarVez()) #Como o ganhador foi o último jogador, então é necessário revezar a vez para o último jogador.
        print("O ganhador é ", tabuleiro_velha.getNomeJogadorDaVez())
        break
    if not tabuleiro_velha.isCasasDisponiveis(): #Se ninguém tiver ganho, então é verificado se o tabuleiro ainda possui casas disponíveis.
        print("Não houve ganhadores! Empate!")
        break
    print("Vez dê ", tabuleiro_velha.getNomeJogadorDaVez())
    jogada = ""
    if tabuleiro_velha.getNomeJogadorDaVez() == jogador_1.getNome():
        jogada = input("Digite sua jogada: ")
    else:
        movimento_CPU = CPU.getMovimentoCPU()
        jogada = tabuleiro_velha.getListKeysDecodificador()[movimento_CPU]
    tabuleiro_velha.setJogada(jogada)
```

## 2.3. CPU vs CPU 🤖

Os passos para fazer um jogo de CPU vs CPU são os mesmos anteriores, alterando somente os jogadores a serem inseridos e a vez de quem deve jogar.

### 2.3.1. Importando e criando as CPU's.

Será necessário importar as CPU's, criar os objetos delas e então inserir elas no tabuleiro como jogadoras.

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.cpu import CPU
tabuleiro_velha = Tabuleiro()
CPU_1 = CPU("CPU 1", "X")
CPU_2 = CPU("CPU 2", "O")
tabuleiro_velha.setJogadores(CPU_1)
tabuleiro_velha.setJogadores(CPU_2)
```

### 2.3.2. Definindo jogadas das CPU's

Agora basta verificar se é a vez da CPU_1 ou da CPU_2 e então definir a jogada de ambas.

```python
movimento_CPU = 0
jogada = ""
if tabuleiro_velha.getNomeJogadorDaVez() == CPU_1:
    movimento_CPU = CPU_1.getMovimentoCPU()
else:
    movimento_CPU = CPU_2.getMovimentoCPU()
jogada = tabuleiro_velha.getListKeysDecodificador()[movimento_CPU]
```

### 2.3.3. Código de CPU vs CPU

Substituindo agora a forma de definir a jogada nos códigos anteriores, teremos o resultado abaixo:

```python
from Tabuleiro.tabuleiro import Tabuleiro
from Tabuleiro.cpu import CPU
tabuleiro_velha = Tabuleiro()
CPU_1 = CPU("CPU 1", "X")
CPU_2 = CPU("CPU 2", "O")
tabuleiro_velha.setJogadores(CPU_1)
tabuleiro_velha.setJogadores(CPU_2)
while True: 
    print(tabuleiro_velha.MostrarTabuleiro())
    if tabuleiro_velha.isGanhador(): #A cada jogada realizada será verificado se houve um ganhador
        tabuleiro_velha.setVez(tabuleiro_velha.RevezarVez()) #Como o ganhador foi o último jogador, então é necessário revezar a vez para o último jogador.
        print("O ganhador é ", tabuleiro_velha.getNomeJogadorDaVez())
        break
    if not tabuleiro_velha.isCasasDisponiveis(): #Se ninguém tiver ganho, então é verificado se o tabuleiro ainda possui casas disponíveis.
        print("Não houve ganhadores! Empate!")
        break
    print("Vez dê ", tabuleiro_velha.getNomeJogadorDaVez())
    movimento_CPU = 0
    jogada = ""
    if tabuleiro_velha.getNomeJogadorDaVez() == CPU_1:
        movimento_CPU = CPU_1.getMovimentoCPU()
    else:
        movimento_CPU = CPU_2.getMovimentoCPU()
    jogada = tabuleiro_velha.getListKeysDecodificador()[movimento_CPU]
    tabuleiro_velha.setJogada(jogada)
```

# 3. RODANDO JOGO PRONTO

Caso deseje apenas testar as funcionalidades, você pode iniciar um jogo já criado que vem junto do pacote. Para isso será necessário você importar o módulo Jogo.py do pacote Jogo.

```python
from Jogo import Jogo
```

Após a importação basta utilizar a função Play() do módulo Jogo.

```python
from Jogo import Jogo

Jogo.Play()
```