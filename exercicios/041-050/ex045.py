#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('-=' * 3, ' JOKENPÔ ', '=-' * 3)
jogador = int(input('Escolha:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n')) - 1
maquina = randint(0, 2)
print('Você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[maquina]))
print('Resultado:', end=" ")
if jogador == maquina:
    print('EMPATE!')
elif (jogador == 0 and maquina == 1) or (jogador == 1 and maquina == 2) or (jogador == 2 and maquina == 0):
    print('você PERDEU')
else:
    print('você VENCEU')
