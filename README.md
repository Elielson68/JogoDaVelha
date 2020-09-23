# JogoDaVelha
Este é um pacote de jogo da velha desenvolvido em python utilizando conceitos de orientação a objetos.

# 1. INSTALAÇÃO

## 1.1. Como baixar o jogo em pacote via pip.
Para instalar a biblioteca via gerenciador de pacotes basta rodar o comando abaixo em seu terminal:

    pip install JogoDaVelha-Elielson68
   
E então a biblioteca principal estará disponível para você montar seu jogo a seu estilo.
Abaixo em  <b>Criando seu jogo</b> há mais explicações sobre.

## 1.2. Como baixar o projeto completo do github.

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
    print(tabu.MostrarTabuleiro())
    if tabu.isGanhador(): #A cada jogada realizada será verificado se houve um ganhador
        tabu.setVez(tabu.RevezarVez()) #Como o ganhador foi o último jogador, então é necessário revezar a vez para o último jogador.
        print("O ganhador é ", tabu.getNomeJogadorDaVez())
    if not tabu.isCasasDisponiveis(): #Se ninguém tiver ganho, então é verificado se o tabuleiro ainda possui casas disponíveis.
        print("Não houve ganhadores! Empate!")
    print("Vez dê ", tabu.getNomeJogadorDaVez())
        jogada = input("Digite sua jogada: ")
        tabu.setJogada(jogada)
```
