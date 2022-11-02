#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal
import math

num = int(input('Digite o número para converter: '))
print('1- binário; 2- octal; 3- hexadecimal')
base = int(input('Selecione a base de conversão: '))
if base == 1:
    print('O número {} em binário é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Base inválida!')
