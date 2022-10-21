#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
#com 15% de aumento

PORCENTAGEM_AUMENTO = 15
salario = float(input('Digite o salário atual: R$'))
print('Com o aumento de {}%, o salário de R${:.2f} passa a ser de\nR${:.2f}'.format(PORCENTAGEM_AUMENTO, salario, salario + (salario * PORCENTAGEM_AUMENTO / 100)))
