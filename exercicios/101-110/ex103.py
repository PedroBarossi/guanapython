""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente. """

def ficha(jogador = '<desconhecido>', gols = '0'):
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {jogador} fez {gols} gols.')

ficha('Zezinho', '3')
ficha('Armando')
ficha(gols= '8')
ficha('Ruibson', 'sete')
