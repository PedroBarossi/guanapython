""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições. """

def voto(nasc):
    from datetime import date
    hoje = date.today()
    anoAtual = hoje.year
    idade = (anoAtual - nasc)
    if (idade) < 16:
        return('Voto NEGADO')
    elif (16 <= idade < 18) or (idade > 65):
        return('Voto OPCIONAL')
    else:
        return('Voto OBRIGATÓRIO')

#TESTES
print(voto(1989)) #33
print(voto(2011)) #12
print(voto(1953)) #70
print(voto(2007)) #16
