n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s+=n
print('A soma vale {}'.format(s)) #soma a flag

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #interrompe o while antes de somar
    s+=n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #FString, atualização Python 3.6+
