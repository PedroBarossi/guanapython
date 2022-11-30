""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista """

lista = [int(input('Digite o primeiro número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: ')),
        int(input('Digite o quinto número: '))]
maior = max(lista)
menor = min(lista)
print(lista)
print(f'O maior valor digitado foi {maior} e está na posição {lista.index(maior)}')
print(f'O menor número digitado foi {menor} e está na posição {lista.index(menor)}')

#Solução Guanabara -> mostrar múltiplas posições

""" listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(listanum)
print(f'O maior valor foi {mai} nas posições ', end="")
for c, i in enumerate(listanum):
    if i == mai:
        print(f'{c}... ', end="")
print(f'\nO menor valor foi {men} nas posições ', end="")
for c, i in enumerate(listanum):
    if i == men:
        print(f'{c}... ', end="")
 """