""" Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira
todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando. """

from utilidadescev import moeda

val = float(input('Digite um valor para ser processado: R$'))
moeda.resumo(val, 80, 35)