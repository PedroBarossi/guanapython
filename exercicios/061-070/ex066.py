""" Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre elas (desconsiderando o flag). """

contador = soma = 0
while True: 
    num = int(input('Digite um número: [999 para sair] '))
    if num == 999:
        break
    soma += num
    contador +=1
print(f'Você digitou {contador} números e a soma deles é {soma}')
