""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """

cadastro = list()
media = 0
mulheres = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F/N] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MFN':
            break
        print('ERRO! Por favor, digite apenas M (masculino), F (feminino) ou N (não-binário)')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    cadastro.append(pessoa)
    print(f"{pessoa['nome']} cadastrado(a)!")
    while True:
        opcao = str(input('Deseja cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Por favor, digite apenas S (sim) ou N (não)')
    if opcao == 'N':
        break
media /= len(cadastro)
print('-=' * 30)
print(f'{"fim do cadastro".upper():^60}')
print('-=' * 30)
print(f"Quantidade de pessoas cadastradas: {len(cadastro)}")
print(f"Média de idade: {media:5.2f}")
print(f"Lista das mulheres cadastradas: {mulheres}")
acimaDaMedia = list()
for p in cadastro:
    if p['idade'] > media:
        acimaDaMedia.append(p['nome'])
print(f"Lista de pessoas acima da média de idade: {acimaDaMedia}")
