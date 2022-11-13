""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120 """

num = int(input('Digite um número para descobrir seu fatorial: '))
fat = 1
while num > 0:
    print('{}'.format(num), end="")
    print(' X ' if num > 1 else ' = ', end="")
    fat *= num
    num -= 1
print('{}'.format(fat))

#Com for

fat = num = int(input('Digite um número para descobrir seu fatorial: '))
print('{}! = '.format(num, num), end="")
for i in range (num, 1, -1):
    print('{} X '.format(i), end="")
    fat *= (i - 1)
print('1 = {}'.format(fat))

#Módulo

from math import factorial
alt = int(input('Digite um número para descobrir seu fatorial: '))
print('O fatorial de {} é {}'.format(alt, factorial(alt)))
