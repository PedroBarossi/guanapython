#Escreva um programa que faça o computador “pensar” em um número inteiro entre
#0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

alvo = randint(0, 5)
tentativa = int(input('Estou pensando num número de 0 a 5, qual? '))
if (tentativa == alvo):
    print('Acertou!! Eu pensei no número {}'. format(alvo))
else:
    print('Errou! Você disse {}, mas eu pensei {}'.format(tentativa, alvo))
