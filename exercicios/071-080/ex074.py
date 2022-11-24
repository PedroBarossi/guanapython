""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. """

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = maior = 0
for i in range(0, len(tupla)):
    if i == 0:
        maior = menor = tupla[i]
    else:
        if tupla[i] < menor:
            menor = tupla[i]
        if tupla[i] > maior:
            maior = tupla[i]
print(tupla)
print(f'O menor valor da tupla é {menor} e o maior valor é {maior}')
#alternativa com métodos Python
print(f'Menor = {min(tupla)}\nMaior = {max(tupla)}')
