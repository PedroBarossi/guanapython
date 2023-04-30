""" Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado. """

import moeda

valor = float(input('Digite um valor para modificá-lo: R$'))
print(f'O valor de {moeda.moeda(valor)} aumentado em 10% é igual a {moeda.moeda(moeda.aumentar(valor))}')
print(f'O valor de {moeda.moeda(valor)} diminuído em 10% é igual a {moeda.moeda(moeda.diminuir(valor))}')
print(f'O dobro do valor {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade do valor {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
