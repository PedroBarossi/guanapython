""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense """

#data = 21/11/2022
classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
                'Athletico-PR', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América-MG',
                'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
                'Atlético Goianiense', 'Avaí', 'Juventude')
print(f'Os primeiros cinco colocados são: {classificacao[:5]}')
print(f'Os quatro últimos colocados são: {classificacao[-4:]}')
print(f'Ordem alfabética: {sorted(classificacao)}')
""" if 'Chapecoense' in classificacao:
    print(f'O time da Chapecoense está na posição {classificacao.index('Chapecoense')}')
else:
    print('O time da Chapecoense não está nesta divisão') """
# O código acima apresenta erro pois esse é o comportamento da tupla quando não há item correspondente
print(f'A time do Avaí está na {classificacao.index("Avaí") + 1}ª posição')
