""" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. """

def leiaInt(mensagem = 'Digite um número: '):
    try:
        entrada = int(input(f'{mensagem}'))
    except ValueError:
        print('ERRO! Por favor digite um número inteiro.')
        entrada = leiaInt(mensagem)
        return entrada
    else:
        return entrada

def leiaFloat(mensagem = 'Digite um número: '):
    try:
        entrada = float(input(f'{mensagem}'))
    except ValueError:
        print('ERRO! Por favor digite um número válido.')
        entrada = leiaFloat(mensagem)
        return entrada
    else:
        return entrada

n = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi {n} e o número real foi {n2}')
