""" Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.  """

print('Vamos montar uma progressão aritmética!')
inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
print('[', end=" ")
while contador <= 10:
    print('{}'.format(inicio), end=" ")
    inicio += razao
    contador += 1
print(']')
opcao = str(input('Deseja mostrar mais termos? (S/N) ')).strip().upper()[0]
while opcao != 'N':
    contador = int(input('Quantos termos? '))
    print('[', end=" ")
    while contador > 0:
        print('{}'.format(inicio), end=" ")
        inicio += razao
        contador -= 1
    print(']')
    opcao = str(input('Deseja mostrar mais termos? (S/N) ')).strip().upper()[0]
print('Até logo!')
