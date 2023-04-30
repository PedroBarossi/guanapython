def aumentar(num, taxa=10):
    retorno = num + (num * taxa / 100)
    return(retorno)


def diminuir(num, taxa=10):
    retorno = num - (num * taxa / 100)
    return(retorno)


def dobro(num):
    retorno = num * 2
    return(retorno)


def metade(num):
    retorno = num / 2
    return(retorno)

def moeda(valor, moeda='R$'):
    return(f'{moeda}{valor:.2f}').replace('.',',')
