def aumentar(num):
    retorno = num + (num * .1)
    return(f'O valor R${num:.2f} aumentado em 10% fica R${retorno:.2f}')


def diminuir(num):
    retorno = num - (num * .1)
    return(f'O valor R${num:.2f} diminuído em 10% fica R${retorno:.2f}')


def dobro(num):
    retorno = num * 2
    return(f'O dobro do valor R${num:.2f} é R${retorno:.2f}')


def metade(num):
    retorno = num / 2
    return(f'A metade do valor R${num:.2f} é R${retorno:.2f}')
