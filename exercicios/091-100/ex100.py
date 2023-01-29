""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior. """

from random import randint
from time import sleep


def sorteia(list):
    for i in range(0, 5):
        list.append(randint(1, 50))
    print(f'Os números sorteados foram: {numeros}')

def somaPar(list):
    soma = 0
    print('Elementos pares da lista:', end=' ')
    for elemento in list:
        if elemento % 2 == 0:
            soma += elemento
            print(f'{elemento}', end=' ', flush=True)
        sleep(.5)
    print(f'\nA soma desses elementos é {soma}')


numeros = []
sorteia(numeros)
sleep(.5)
somaPar(numeros)
