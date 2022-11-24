""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais. """

tupla = ('alegria', 'piscina', 'ovo', 'paçoca', 'baleia',
         'anagrama', 'espelho', 'bule', 'esquina')
vogais = 'aeiou'
for palavra in tupla:
    print(f'{palavra.upper()} tem as vogais:', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(f'{letra}', end=' ')
    print('')
