""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

jogador = {}
jogador['nome'] = str(input("Nome: ")).strip()
jogador['partidas'] = int(input("Partidas jogadas: "))
jogador['listaGols'] = []
for i in range(1, jogador['partidas']+1):
    gols = int(input(f"Gols na partida {i}: "))
    jogador['listaGols'].append(gols)
jogador['totalGols'] = sum(jogador['listaGols'])
for k, v in jogador.items():
    print(f"- {k} tem valor {v}")

#Desafio Guanabara
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for i in range(1, jogador['partidas']+1):
    print(f"    => Na partida {i}, fez {jogador['listaGols'][i-1]} gols.")
print(f'Somando um total de {jogador["totalGols"]} gols.')
