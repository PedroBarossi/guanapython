lanche = ['suco', 'hamburguer', 'pizza', 'cookie']
lanche.append('sorvete')
lanche.insert(0, 'hotdog')
lanche.pop()
if 'cookie' in lanche:
    lanche.remove('cookie')
print(lanche)

num = list(range(4, 11))
num[0] = 11
num.insert(2, 18)
num.append(12)
num.sort(reverse=True)
num.remove(9) #parâmetro indica valor
num.pop(1) #pop sem nada remove o último, parâmetro indica posição
for n in num:
    print(n, end=' ')
print(f'\nEssa lista tem {len(num)} elementos')
for c, i in enumerate(lanche):
    print(f'Na posição {c} vou comer o lanche {i}')

#b = a cria uma ligação entre as listas (alterar uma altera a outra)
#b = a[:] "copia" os elementos de uma para a outra
