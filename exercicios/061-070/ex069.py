""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.  """

contadorTotal = 1
maior = homem = mulherSub20 = 0
while True:
    print(f'{contadorTotal}ª Pessoa')
    idade = int(input('Informe a idade: '))
    if idade > 18:
        maior += 1
    while True:
        sexo = str(input('Informe o sexo: [M/F/N] ')).strip().upper()[0]
        if sexo in 'MFN':
            break
        else:
            print('Inválido! Tente novamente.')
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherSub20 += 1
    opcao = str(input('Deseja cadastrar mais uma pessoa? (N para sair) ')).strip().upper()[0]
    if opcao == "N":
        break
    contadorTotal += 1
print(f"""TOTAL CADASTRADO: {contadorTotal}
Pessoas acima de 18 anos: {maior}
Quantidade de homens: {homem}
Mulheres abaixo de 20 anos: {mulherSub20}
FIM DO PROGRAMA""")
