# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 < n2:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
n3 = int(input('Digite o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('Números digitados: {}, {} e {}'. format(n1, n2, n3))
print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
