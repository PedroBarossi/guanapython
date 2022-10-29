#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
#da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

dist = int(input('Qual a distância da sua viagem? '))
if dist <= 200:
    print('Custo da viagem: R${:.2f}'.format(dist * .5))
    print('Calculado a partir da distância {}km a R$0,50 por km'.format(dist))
else:
    print('Custo da viagem: R${:.2f}'.format(dist * .45))
    print('Calculado a partir da distância {}km a R$0,45 por km'.format(dist))
