""" Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """

separados = [list(), list()]
for i in range(0, 7):
    num = (int(input(f'{i+1}º número: ')))
    if num % 2 == 0:
        separados[0].append(num)
    else:
        separados[1].append(num)
separados[0].sort()
separados[1].sort()
print(f'Números pares: {separados[0]}')
print(f'Números ímpares: {separados[1]}')
