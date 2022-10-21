#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite o valor em metros: '))
print('O valor digitado pode ser expresso como {}m, {:.0f}cm ou {:.0f}mm'.format(m, m * 100, m * 1000))
