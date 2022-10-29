#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
#uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

limite = 80
velocidade = int(input('Qual foi a velocidade do veículo (em Km/h)? '))
if (velocidade > limite):
    print('Oh-oh! Acima do limite! ({}km/h)'.format(limite))
    print('Você foi multado em R${:.2f}'.format((velocidade - limite) * 7))
else:
    print('Continue dirigindo com segurança.')
