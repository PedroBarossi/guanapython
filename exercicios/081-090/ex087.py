""" Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Posição [{i},{j}]: '))
print('-='*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            somaTerceira += matriz[i][j]
    print()
maiorSegunda = max(matriz[1])
print(f'Soma de todos os pares = {somaPares}')
print(f'Soma da terceira coluna = {somaTerceira}')
print(f'Maior valor da segunda linha = {maiorSegunda}')
