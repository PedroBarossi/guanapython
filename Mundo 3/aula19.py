#dados = dict()
dados = {'nome': 'Pedro',
        'idade': 25}
dados['sexo'] = 'M'
del dados['idade']
filme = {'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
locadora = list()
locadora.append(filme)
locadora.append({'titulo': 'Avengers',
                'ano': 2012,
                'diretor': 'Joss Whedon'})
locadora.append({'titulo':'Matrix',
                'ano': 1999,
                'diretor': 'Wachowski'})
#print(locadora)
for num, item in enumerate(locadora):
    print(f'{num + 1}º filme:')
    for k, v in item.items():
        print(f'O {k} é {v}')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #método copy => não é possível fatiar dicionário
print(brasil)
