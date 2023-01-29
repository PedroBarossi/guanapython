""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """

def maior(*col):
    if len(col) == 0:
        print('Não foi informado nenhum valor')
    else:
        retornar = 0
        for i in range(0, len(col)):
            if i == 0:
                retornar = col[i]
            else:
                if col[i] > retornar:
                    retornar = col[i]
        print(f'O maior número entre {col} é {retornar}')


maior(1, 2, 5)
maior(18, -3)
maior(-1, -4, -6)
maior(48, 66, 4, 140, 7, 140, 18, 2023)
maior()
