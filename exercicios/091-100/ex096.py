""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno. """

def area(l, c):
    a = l * c
    return a


larg = float(input('Largura do terreno (m): '))
comp = float(input('Comprimento do terreno (m): '))
print(f'A área de um terreno com {larg}m de largura e {comp}m de comprimento é {area(larg, comp)}m²')
