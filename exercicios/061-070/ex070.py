""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.  """

totalProdutos = 1
totalPreco = maisDeMil = menorPreco = nomeMenorPreco = 0
while True:
    print(f'Cadastrando o {totalProdutos}° produto')
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    totalPreco += preco
    if preco > 1000:
        maisDeMil += 1
    if totalProdutos == 1 or preco < menorPreco:
        menorPreco = preco
        nomeMenorPreco = nome
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Opção inválida! Tente novamente')
        else:
            break
    if opcao == 'N':
        break
    totalProdutos += 1
print('FIM DAS COMPRAS')
print(f'Valor total: R${totalPreco:.2f}')
print(f'A compra tem {maisDeMil} produto(s) acima de R$1000,00')
print(f'O produto mais barato foi {nomeMenorPreco}')
