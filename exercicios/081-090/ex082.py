""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas. """

lista = []
while True:
    lista.append(int(input('Digite um número para adicioná-lo à lista: ')))
    while True:
        opcao = str(input('Deseja adicionar outro número? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        else:
            print(f'Opção {opcao} inválida, tente novamente.')
    if opcao == 'N':
        break
#o método acima foi reusado de exercícios anteriores
print(f'Lista original: {lista}')
par = []
impar = []
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Números pares: {par}\nNúmeros ímpares: {impar}')
