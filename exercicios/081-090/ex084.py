""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """

#cadastrando
pessoas = []
while True:
    cadastrar = [] #atribuindo vazio sempre que inicia o loop, dispensa o uso do .clear()
    cadastrar.append(str(input('Informe o nome da pessoa: ')).strip())
    cadastrar.append(float(input('Informe o peso da pessoa: (kg) ')))
    pessoas.append(cadastrar[:])
    escolha = str(input('Deseja cadastrar mais uma pessoa? [N para sair] ')).strip().upper()[0]
    if escolha == 'N':
        break

#percorrendo para descobrir o maior e menor pesos
maior = menor = 0
for p in pessoas:
    if p[1] < menor or menor == 0:
        menor = p[1]
    if p[1] > maior:
        maior = p[1]

#povoando as listas de pessoas mais e menos pesadas
maisPesadas = []
menosPesadas = []
for p in pessoas:
    if p[1] == menor:
        menosPesadas.append(p[0])
    if p[1] == maior:
        maisPesadas.append(p[0])

print('-=' * 20)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Pessoas mais pesadas: {maisPesadas} com {maior}Kg')
print(f'Pessoas menos pesadas: {menosPesadas} com {menor}Kg')
