""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável. """

def escreva(texto):
    print('~' * (len(texto) + 2))
    print(f' {texto} ')
    print('~' * (len(texto) + 2))


escreva('Olá, Mundo!')
escreva('Essa é a função escreva()')
escreva('lobo')
