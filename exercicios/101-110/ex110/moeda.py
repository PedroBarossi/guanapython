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

def resumo(valor=0, aum=10, dim=5):
    print(f'-=' * 20)
    print(f'{"Resumo de operações":^40}'.upper())
    print(f'-=' * 20)
    print(f'{"Valor analisado":<20}{moeda(valor):>20}')
    print(f'{"Dobro":<20}{dobro(valor):>20}')
    print(f'{"Metade":<20}{metade(valor):>20}')
    print(f'{aum:<2}{"% de aumento":<18}{aumentar(valor, aum):>20}')
    print(f'{dim:<2}{"% de redução":<18}{diminuir(valor, dim):>20}')
    print(f'-=' * 20)