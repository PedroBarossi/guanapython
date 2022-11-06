""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o """

soma = 0
contador = 0
for i in range(0, 6):
    atual = int(input('Digite o {}° número: '.format(i+1)))
    if atual % 2 == 0:
        soma += atual
        contador += 1
print('A soma dos {} valores pares digitados é igual a {}'.format(contador, soma))
