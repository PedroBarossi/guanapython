#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
separado = nome.split()
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras (sem espaços): {}'.format(len(''.join(separado))))
# ou len.nome - nome.count(' ') -> comprimento da string menos número de espaços
print('Quantidade de letras do primeiro nome: {}'.format(len(separado[0])))
# ou nome.find(' ') -> vai dizer a posição do primeiro espaço
