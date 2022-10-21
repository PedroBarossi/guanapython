#Faça um programa que leia um número inteiro e mostre na tela
#seu sucessor e seu antecessor

valor = int(input('Digite um valor: '))
print('O valor digitado foi {}. \nSeu antecessor é {} e seu sucessor é {}'.format(valor, valor - 1, valor + 1))
