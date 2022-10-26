#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = input('Digite o nome de uma cidade: ') #.strip()
separado = cidade.split()
print('O nome da cidade começa com "SANTO"? {}'.format('SANTO' in separado[0].upper()))
#ou cidade[:5].upper() == 'SANTO'
