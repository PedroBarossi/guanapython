""" Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada """

from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i > f:
        while i >= f:
            print(i, end=' ', flush=True)
            sleep(.2)
            i -= p
    else:
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(.2)
            i += p
    print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))
contador(inicio, fim, passo)
