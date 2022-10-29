#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

antes = float(input('Digite o salário atual: R$'))
if antes > 1250:
    aumento = 10
else:
    aumento = 15
print('O salário de R${:.2f} terá um aumento de {}% e passará a ser R${:.2f}'.format(antes, aumento, (antes * aumento / 100 + antes)))
