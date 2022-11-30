""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente. """

unicos = []
while True:
    num = int(input('Digite um número para adicioná-lo à lista: '))
    if num not in unicos:
        unicos.append(num)
        print('Número adicionado!')
    else:
        print('Esse número não foi adicionado pois já está na lista')
    escolha = str(input('Deseja adicionar outro número? [N para sair] ')).strip().upper()[0]
    if escolha == 'N':
        break
unicos.sort()
print(f'Os números digitados foram {unicos}')
