""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input('Digite uma frase:\n')).strip().upper()
palavras = frase.split()
semEspaco = ''.join(palavras)
inverso = ''
for letra in range(len(semEspaco)- 1, -1, -1):
    inverso += semEspaco[letra] # == semEspaco[::-1]
print('O inverso de {} é {}'.format(semEspaco, inverso))
if semEspaco == inverso:
    print('Essa frase É UM PALÍNDROMO')
else:
    print('Essa frase NÃO É UM PALÍNDROMO')
