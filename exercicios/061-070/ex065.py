""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores. """

contador = soma = maior = menor = 0
opcao = ""
while opcao != 'N':
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Deseja informar outro valor? [S/N] ')).strip().upper()[0]
print('A média dos valores digitados foi {}'.format(soma / contador))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
