""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. """

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
print(f'Lista: {lista}')
print(f'Quantidade de números: {len(lista)}')
lista.sort(reverse=True)
print(f'Valores em ordem decrescente: {lista}')
if 5 not in lista:
    print('O valor 5 não está presente na lista')
else:
    print(f'O valor 5 aparece {lista.count(5)} vez(es) na lista')
