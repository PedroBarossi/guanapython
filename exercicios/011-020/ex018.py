#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse ângulo
import math

angulo = int(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Ângulo: {}º\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(angulo, seno, cosseno, tangente))
