""" Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores """

from datetime import date

anoAtual = date.today().year
menores = 0
maiores = 0
for i in range(1, 8):
    nasc = (int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i))))
    if anoAtual - nasc >= 18:
        maiores += 1
    else:
        menores += 1
print('Dessas sete pessoas, {} são menores de idade e {} são maiores'.format(menores, maiores))
