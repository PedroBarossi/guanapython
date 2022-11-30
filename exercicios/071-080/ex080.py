""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. """

valores = list()
for i in range(1, 6):
    num = int(input(f'Digite o {i}º número: '))
    if i == 1:
        valores.append(num)
        print('Adicionado no final da lista')
    else:
        for j in range(0, len(valores)):
            if num <= valores[j]:
                valores.insert(j, num)
                print(f'Adicionado na posição {j}')
                break
            elif j == len(valores)-1:
                valores.append(num)
                print('Adicionado no final da lista')
print(valores)

#Solução Guanabara - Simplificando a lógica de adicionar os números

""" if i == 1 or i > valores[-1]:
    valores.append(num)
    print('Adicionado no final da lista')
else: 
    pos = 0
    while pos < len(valores):
        if num <= valores[pos]:
            valores.insert(pos, num)
            break 
        pos += 1"""
