""" Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes """

reta1 = float(input('Digite o comprimento da reta 1 (em cm): '))
reta2 = float(input('Digite o comprimento da reta 2 (em cm): '))
reta3 = float(input('Digite o comprimento da reta 3 (em cm): '))
if (reta1 + reta2 < reta3) or (reta2 + reta3 < reta1) or (reta1 + reta3 < reta2):
    print('Com essas retas é IMPOSSÍVEL formar um triângulo')
else:
    print('Com essas retas, é POSSÍVEL formar um triângulo', end=" ")
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif (reta1 == reta2) or (reta2 == reta3) or (reta3 == reta1):
        print('ISÓSCELES')
    else:
        print('ECALENO')
