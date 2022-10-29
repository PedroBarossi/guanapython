#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite um ano para saber se ele é bissexto: '))
if (ano % 4 == 0): #and (ano % 100 != 0) or (ano % 400 == 0)
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))

#BÔNUS : pegar ano atual se for digitado zero
#from datetime import date
#if ano == 0:
#    ano = date.today().year