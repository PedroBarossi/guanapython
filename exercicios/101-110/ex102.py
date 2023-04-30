""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial. """

def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show(opcional): mostra o cálculo na tela
    :return: o valor do fatorial de um número num
    """
    fat = num
    if show:
        print(f'{num}! = {num}', end=' ')
        while num > 1:
            num -= 1
            print(f'X {num}', end= ' ')
            if num == 1:
                print('=', end=' ')
            fat *= num
    else:
        print(f'{num}! =', end=' ')
    while num > 1:
        num -= 1
        fat *= num
    return fat

print(fatorial(5, True))
print(fatorial(8))
print(fatorial(3, False))
print(fatorial(7, True))
help(fatorial)
