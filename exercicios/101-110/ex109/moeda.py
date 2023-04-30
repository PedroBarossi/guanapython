def aumentar(num, taxa=10, format='True'):
    retorno = num + (num * taxa / 100)
    if format:
        return(moeda(retorno))
    else:
        return(retorno)


def diminuir(num, taxa=10, format='True'):
    retorno = num - (num * taxa / 100)
    if format:
        return(moeda(retorno))
    else:
        return(retorno)


def dobro(num, format='True'):
    retorno = num * 2
    if format:
        return(moeda(retorno))
    else:
        return(retorno)


def metade(num, format='True'):
    retorno = num / 2
    if format:
        return(moeda(retorno))
    else:
        return(retorno)

def moeda(valor, moeda='R$'):
    return(f'{moeda}{valor:.2f}').replace('.',',')
