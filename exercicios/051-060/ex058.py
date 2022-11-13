""" Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer. """

from random import randint

maquina = randint(0, 10)
tentativas = 1
print('Estou pensando num número entre 0 a 10...')
jogador = int(input('Tente adivinhar qual: '))
while jogador != maquina:
    print('Errou!', end='')
    if jogador < maquina: #
        print('Tente um número mais alto...') #
    else: #
        print('Tente um número mais baixo...') #
    tentativas += 1
    jogador = int(input('Tente novamente: '))
print('Acertou! Eu pensei no número {}'.format(maquina))
print('Você precisou de {} tentativa(s) para acertar.'.format(tentativas))

#Sugestão do Guanabara: adicionar dica se o palpite é menor ou maior