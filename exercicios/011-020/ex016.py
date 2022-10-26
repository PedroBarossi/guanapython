#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
from math import trunc

real = float(input('Digite um número real: '))
inteira = trunc(real)
print('A porção inteira de {} é {}'.format(real, inteira))
