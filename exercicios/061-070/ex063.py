""" Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8  """

termos = int(input('Exibir quantos elementos da Sequência de Fibonacci? '))
atual = 0
anterior = 0
i = 1
while i <= termos:
    print(atual, end= " ")
    if i <= 2:
        anterior = atual
        if i == 1:
            atual += 1
    else:
        aux = anterior + atual
        anterior = atual
        atual = aux
    i += 1

#Diferente da solução apresentada no vídeo, esta forma permite exibir menos que 3 termos