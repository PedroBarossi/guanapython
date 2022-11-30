dados = list()
dados.append('Pedro')
dados.append(33)
print(dados[0]) #Pedro

pessoas = list()
pessoas.append(dados[:]) #<---importante
pessoas.append(['Maria', 19])
pessoas.append(['João', 32])
print(pessoas)
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1]) #['Maria', 19]

galera = [['Gustavo', 40], ['Joaquim', 13], ["Ana", 25]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #<--- importante
print(galera)
maior = menor = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores.')
