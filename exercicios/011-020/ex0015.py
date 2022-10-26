#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input('Informe a quantidade de Km rodados: '))
dias = int(input('Informe a quantidade de dias de aluguel: '))
totalkm = km * 0.15
totaldias = dias * 60
print('{} dias de aluguel a R$60.00/dia: R${:.2f}'.format(dias, totaldias))
print('{} kilômetros rodados a R$0.15/km: R${:.2f}'.format(km, totalkm))
print('Total a pagar: R${:.2f}'.format(totalkm + totaldias))
