#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um valor: '))
print('Valor digitado: {}\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.3f}'.format(numero, numero * 2, numero * 3, numero ** (1/2)))
