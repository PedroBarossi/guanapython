for i in range(1, 11):
    print(i, end=" ")
print('Fim')

for i in range(6, 0, -1):
    print(i, end=" ")
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')