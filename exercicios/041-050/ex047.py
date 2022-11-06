#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

#Solução 1
for i in range(2, 52, 2):
    print(i, end=" ")

print('\n------')

#Solução 2
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
