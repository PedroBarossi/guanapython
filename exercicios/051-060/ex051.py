""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão. """

print('Vamos montar uma Progressão Aritmética!')
inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
print('Os primeiros 10 termos da sua PA são: \n{', end=" ")
for i in range(0, 10):
    print('{}'.format(inicio), end=" ")
    inicio += razao
print('}')
