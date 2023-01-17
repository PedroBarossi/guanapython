""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. """
from datetime import date

anoAtual = date.today().year
funcionario = dict()
print("-+-" * 20)
print(f"{'CADASTRO DE FUNCIONÁRIO':^60}")
print("-+-" * 20)
funcionario["nome"] = str(input('Nome: ')).strip()
funcionario["nascimento"] = int(input('Ano de nascimento: '))
funcionario["idade"] = anoAtual - funcionario["nascimento"]
funcionario["ctps"] = int(input('CTPS: [Se não tiver, digite 0]'))
if funcionario["ctps"] != 0:
    funcionario["contratacao"] = int(input('Ano de contratação: '))
    funcionario["salario"] = float(input('Salário: R$'))
    funcionario["aposentadoria"] = anoAtual - funcionario["contratacao"] + 35
print("-+-" * 20)
print(f"{'DADOS DO FUNCIONÁRIO':^60}")
print("-+-" * 20)
for k, v in funcionario.items():
    print(f'- {k.capitalize()} tem o valor {v}')
