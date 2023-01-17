""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o 
vencedor tirou o maior número no dado. """

from random import randint
from time import sleep
from operator import itemgetter

jogos = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    sleep(.5)
ranking = dict()
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING ==')
for i, j in enumerate(ranking):
    print(f'{i+1}º lugar: {j[0]} com o resultado {j[1]}')
    sleep(.5)
