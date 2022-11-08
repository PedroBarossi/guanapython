""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos """

menor = 0
maior = 0
for pessoas in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(pessoas)))
    if (peso < menor) or (menor == 0):
        menor = peso
    if peso > maior:
        maior = peso
print('O MENOR peso foi {}Kg e o MAIOR peso foi {}Kg.'.format(menor, maior))
