#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
#exceder 30% do salário ou então o empréstimo será negado.
print('-='*20)
print('Vamos analisar seu empréstimo...')
print('-='*20)
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite sua renda mensal: R$'))
prazo = int(input('Digite em quantos anos planeja pagar: '))
prestacao = valor / (prazo * 12)
if prestacao <= (salario * .3):
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')
