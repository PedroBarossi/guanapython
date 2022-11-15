""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo. """

while True:
    num = int(input('Digite um número para ver sua tabuada:\n(ou um número negativo para sair) '))
    if num < 0:
        print('Até logo!')
        break
    for i in range (1, 11):
        print(f'{num} X {i:2} = {num * i}')
