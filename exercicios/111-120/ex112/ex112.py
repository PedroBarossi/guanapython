""" Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma
função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação
de dados para aceitar apenas valores que seja monetários. """

from utilidadescev import dado
from utilidadescev import moeda

val = dado.leiaDinheiro('Digite um valor para ser processado: R$')
moeda.resumo(val, 80, 35)