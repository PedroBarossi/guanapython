""" Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108 """

import moeda

valor = float(input('Digite um valor para modificá-lo: R$'))
print(f'O valor de {moeda.moeda(valor)} aumentado em 10% é igual a {moeda.aumentar(valor)}')
print(f'O valor de {moeda.moeda(valor)} diminuído em 10% é igual a {moeda.diminuir(valor)}')
print(f'O dobro do valor {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'A metade do valor {moeda.moeda(valor)} é {moeda.metade(valor)}')
