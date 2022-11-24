""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular. """

tupla = ('Iogurte', 1.49,
        'Farinha de trigo', 5.16,
        'Óleo de soja', 7.48,
        'Bala de menta', 1.99,
        'Paçoquinha', .55)
#minha estilização
print('-=' * 20)
print('Lista de produtos'.upper().center(40))
print('-=' * 20)
for i in range(0, len(tupla) - 1, 2):
    print(f'{tupla[i]}'.ljust(19), end='|')
    i+=1
    print(f'R${tupla[i]}'.rjust(20))
print('-=' * 20)

#Estilização Guanabara
for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end="")
    else:
        print(f'R${tupla[i]:>6.2f}')
