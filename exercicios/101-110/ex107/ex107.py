""" Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções """

import moeda


valor = float(input('Digite um valor para modificá-lo: R$'))
print(moeda.aumentar(valor))
print(moeda.diminuir(valor))
print(moeda.dobro(valor))
print(moeda.metade(valor))
