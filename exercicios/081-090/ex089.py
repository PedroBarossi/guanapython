""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. """

boletins = list()
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletins.append([nome, [nota1, nota2], media])
    opcao = str(input('Cadastrar outro aluno? [N para sair] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-=' * 20)
print(f"{'BOLETIM':^40}")
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":8}')
for n, aluno in enumerate(boletins):
    print(f'{n:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('_' * 40)
    opcao = int(input("Exibir nota de qual aluno? (999 para parar): "))
    if opcao == 999:
        print('Fim')
        break
    if opcao <= len(boletins) - 1:
        print(f'As notas de {boletins[opcao][0]} são: {boletins[opcao][1]}')
