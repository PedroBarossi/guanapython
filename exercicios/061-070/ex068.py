""" Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """
from random import randint

print('-=-' * 15)
print('PAR OU ÍMPAR'.center(45))
print('-=-' * 15)
vitorias = 0
while True:
    maquina = randint(0, 5)
    while True:
        jogador = int(input('Quantos dedos vai jogar? (0 a 5) '))
        if 0 <= jogador <= 5:
            break
        else:
            print('Número inválido! Tente de novo')
    while True:
        escolha = str(input('Par ou ímpar? (P/I) ')).strip().upper()[0]
        if escolha in 'PI':
            break
        else:
            print('Escolha inválida! Tente novamente.')
    resultado = jogador + maquina
    print(f'Você escolheu {jogador} e o computador escolheu {maquina}, totalizando {resultado}')
    print('Você escolheu', end=" ")
    print('PAR' if escolha == 'P' else 'ÍMPAR')
    if (escolha == 'P' and resultado % 2 == 0) or (escolha == 'I' and resultado % 2 != 0):
        print('VOCÊ GANHOU!')
        vitorias += 1
    else:
        print('VOCÊ PERDEU!')
        break
print(f'O jogo terminou! Vitórias consecutivas: {vitorias}')
