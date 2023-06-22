# Tic-Tac-Toe-3D

## Descrição do Projeto

- O Tic-Tac-Toe 3D é uma versão tridimensional do popular jogo da velha, onde dois jogadores competem para marcar uma linha com suas respectivas peças em um tabuleiro 3D. O objetivo é conseguir uma sequência de três peças em uma linha, seja na horizontal, vertical ou diagonal.

- Para tornar a experiência de jogo mais envolvente, o projeto utiliza a biblioteca pyOpenGl para renderizar o tabuleiro em uma interface gráfica interativa. A manipulação dos elementos 3D, como as peças e o tabuleiro, é feita através dos recursos oferecidos pela pyOpenGl, proporcionando uma experiência visualmente atraente.

- A comunicação entre os dois jogadores é estabelecida por meio de sockets, permitindo que eles se conectem e joguem em rede. Ao iniciar o jogo, o jogador tem a opção de hospedar uma partida, onde o servidor é executado utilizando a biblioteca subprocess, ou entrar em uma partida existente, tornando-se o cliente. A descoberta de partida é feita automaticamente na rede, garantindo que os jogadores possam se encontrar e iniciar uma partida de forma conveniente.

## Requisitos do Projeto

- Python 3.10.7
- Bibliotecas:
  - pyOpenGl
  - subprocess
  - socket

## Como Executar o Jogo

- Clone o repositório do projeto para sua máquina local.
- Certifique-se de ter o Python 3.10 instalado.
- Instale as dependências necessárias, como a biblioteca pyOpenGl, utilizando um - gerenciador de pacotes Python, como o pip.
- Abra um terminal ou prompt de comando e navegue até o diretório do projeto.
- Execute o arquivo principal do jogo (main.py).
- Na interface do jogo, escolha entre hospedar uma partida ou entrar em uma partida existente.
- Divirta-se jogando Tic-Tac-Toe 3D com seus amigos!
