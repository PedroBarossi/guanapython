#Operadores
print(7+2) #9
print(7-2) #5
print(7*2) #14
print(7/2) #3.5
print(7**2) #49
# ou pow(7,2)
print(7//2) #3
print(7%2) #1

#Ordem de precedência
print(5+3*2) #11
print(3*5+4**2) #31
print(3*(5+4)**2) #243

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divI = n1 // n2
exp = n1 ** n2
res = n1 % n2
print('A soma é {} e a diferença é {}.'.format(som, sub), end=' ')
print('O produto é {},\na potência é {} e a divisão exata é {:.3f}'.format(mul, exp, div))
print('A divisão inteira é {}, com resto {}'.format(divI, res))