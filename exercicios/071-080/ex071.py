""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. """

""" PRIMEIRA SOLUÇÃO
saque = restante = int(input('Digite o valor que deseja sacar: R$'))
cedula = 50
tot50 = tot20 = tot10 = tot1 = 0
while True:
    if restante >= cedula:
        restante -= cedula
        tot50 += 1
    else:
        cedula = 20
        while True:
            if restante >= cedula:
                restante -= cedula
                tot20 += 1
            else:
                cedula = 10
                while True:
                    if restante >= cedula:
                        restante -= cedula
                        tot10 += 1
                    else:
                        cedula = 1
                        while True:
                            if restante >= cedula:
                                restante -= cedula
                                tot1 += 1
                            else:
                                break
                        break
                break
        break                   
print(f'Valor solicitado: R${saque:.2f}')
print(f'{tot50} cédulas de R$50')
print(f'{tot20} cédulas de R$20')
print(f'{tot10} cédulas de R$10')
print(f'{tot1} cédulas de R$1') """

saque = restante = int(input('Qual valor deseja sacar? R$'))
cedula = 50
totCedula = 0
while True:
    if restante >= cedula:
        restante -= cedula
        totCedula +=1
    else:
        if totCedula > 0:
            print(f'{totCedula} cédula(s) de R${cedula}')
        if cedula == 50:
            cedula = 20
            totCedula = 0
        elif cedula == 20:
            cedula = 10
            totCedula = 0
        elif cedula == 10:
            cedula = 1
            totCedula = 0
        if restante == 0:
            break
print(f'Total sacado: R${saque}')
