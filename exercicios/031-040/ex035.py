#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo

reta1 = float(input('Digite o comprimento da reta 1 (em cm): '))
reta2 = float(input('Digite o comprimento da reta 2 (em cm): '))
reta3 = float(input('Digite o comprimento da reta 3 (em cm): '))
if (reta1 + reta2 < reta3) or (reta2 + reta3 < reta1) or (reta1 + reta3 < reta2):
    print('Com essas retas é IMPOSSÍVEL formar um triângulo')
else:
    print('É POSSÍVEL formar um triângulo com essas retas')
