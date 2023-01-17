""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """
from random import randint

quantidadeJogos = int(input('Gerar quantos jogos? '))
jogos = list()
for i in range(0, quantidadeJogos):
    jogoAtual = []
    while len(jogoAtual) < 6:
        numAtual = randint(1, 60)
        if numAtual not in jogoAtual:
            jogoAtual.append(numAtual)
    jogos.append(sorted(jogoAtual))
print('Jogos gerados: ')
for jogo in jogos:
    print(jogo)
