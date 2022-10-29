tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')
#print('carro novo' if tempo <= 3 else 'carro velho')
print('---FIM---')

nome = str(input('Qual é o seu nome? '))
if nome == 'Pedro':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 7:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
