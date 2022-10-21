#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possíveis sobre ele

digite = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é', type(digite))
print('É alfabético?', digite.isalpha())
print('É um número?', digite.isnumeric())
print('É alfanumérico?', digite.isalnum())
print('Está em maiúsculas?', digite.isupper())
print('Está em minúsculas?', digite.islower())
print('Só tem espaços?', digite.isspace())
print('Está capitalizado?', digite.istitle())
