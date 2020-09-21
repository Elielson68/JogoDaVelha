# JogoDaVelha


## 1. Como iniciar o jogo
Primeiro baixe o projeto como .zip e extraia o arquivo em uma pasta desejada ou clone usando o comando abaixo em seu prompt de comando:

    git clone https://github.com/Elielson68/JogoDaVelha.git

Abra seu prompt de comando na pasta JogoDaVelha e então rode o comando:

    python PlayJogo.py
   
## 2. Como jogar

O tabuleiro possui este formato abaixo:

    	 1	 2	 3
    A: 	[-]	[-]	[-]	
    B: 	[-]	[-]	[-]	
    C: 	[-]	[-]	[-]	
Para fazer uma jogada basta indicar a linha, que são representadas pelas letras A, B e C. E logo em seguida indicar a coluna, representada pelos números: 1,2 e 3.

Exemplo de como marcar o primeiro quadrado abaixo:
    
    A1

 Então o seu tabuleiro irá atualizar para o símbolo do jogador da vez, que neste exemplo é o 'X'
 
     	 1	 2	 3
    A: 	[X]	[-]	[-]	
    B: 	[-]	[-]	[-]	
    C: 	[-]	[-]	[-]	

## 3. Como personalizar o jogo
Quando tiver iniciado o jogo, você pode escolher a opção 3 do menu que dá a opção de você personalizar o nome dos dois players (que por padrão são iniciados como Player 1 e Player 2) ou o nome da CPU. Também é possível alterar o símbolo dos players e da CPU.

## 4. CPU vs CPU

Selecionando a 4 opção do menu, o jogo é jogado apenas por CPU, duas CPU's jogam aleatoriamente e vão registrando as jogadas vitoriosas no arquivo jogadas.txt e a partir daí elas começam a selecionar alguma jogada dentro do arquivo aleatoriamente.