#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
from math import hypot

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipo = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
