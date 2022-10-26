#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print("""Primeiro nome: {}
Último nome: {}""".format(separado[0], separado[len(separado) - 1]))
