""" def mostraLinha():
    print('-' * 30)

mostraLinha()
print(f'{"PRIMEIRA VEZ":^30}')
mostraLinha()
mostraLinha()
print(f'{"SEGUNDA VEZ":^30}')
mostraLinha() """

def titulo(tituloTxt, tamanho):
    print('-' * tamanho)
    print(f'{tituloTxt:^{tamanho}}'.upper())
    print('-' * tamanho)

titulo('primeira vez', 30)
titulo('segunda vez', 40)

# --------------------------------------

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(4, 5)
soma(b=17, a=3)
soma(16, 44)

# --------------------------------------

def contador(*num): # * = desempacotar
    tam = len(num)
    print(f'Recebi os valores {num} que são ao todo {tam} números')

contador(3, 2, 1)
contador(18, 15, 16, 11)
contador(0)

# --------------------------------------

def dobraLista(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobraLista(valores)
print(valores)