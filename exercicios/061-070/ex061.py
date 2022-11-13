""" Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while """

print('Vamos montar uma progressão aritmética!')
inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
print('[', end=" ")
while contador <= 10:
    print('{}'.format(inicio), end=" ")
    inicio += razao
    contador += 1
print(']')
