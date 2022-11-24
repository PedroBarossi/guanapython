#Tuplas são IMUTÁVEIS
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1]) #suco
print(lanche[-1]) #pudim
print(lanche[:2]) #do começo ao 2, excluindo
for comida in lanche:
#for comida in range(0, len(lanche)):
    print(comida)

for pos, comida in enumerate(lanche):
    print(f'{pos} - {comida}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #(2, 5, 4, 5, 8, 1, 2)
print(c.count(5)) #2 vezes
print(c.index(5, 1)) #encontra índice do elemento 5, procurando a partir do índice 1
del(a) #a tupla pode ser apagada completamente
