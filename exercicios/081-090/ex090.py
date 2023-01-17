""" Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. """

aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).strip()
aluno['media'] = float(input('Média: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'REPROVADO'
elif aluno['media'] < 7:
    aluno['situacao'] = 'DE RECUPERAÇÃO'
else:
    aluno['situacao'] = 'APROVADO'
print(f'A média do aluno {aluno["nome"]} é {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')
