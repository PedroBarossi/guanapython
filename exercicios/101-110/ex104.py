""" Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à
função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ') """

def leiaInt(mensagem = 'Digite um número: '):
    while True:
        entrada = str(input(f'{mensagem}'))
        if entrada.isnumeric():
            return int(entrada)
        else:
            print('ERRO: O valor digitado deve ser numérico.')

n = leiaInt('Digite um n: ')
print(n)
