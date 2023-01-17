""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador. """
from time import sleep

jogadores = list()
while True:
    print('-=' * 20)
    print(f"{len(jogadores) + 1}º JOGADOR")
    jogador = dict()
    jogador['nome'] = str(input("Nome: ")).strip()
    jogador['partidas'] = int(input("Partidas jogadas: "))
    jogador['listaGols'] = list()
    for i in range(1, jogador['partidas'] + 1):
        gols = int(input(f"Gols na partida {i}: "))
        jogador['listaGols'].append(gols)
    jogador['totalGols'] = sum(jogador['listaGols'])
    jogador['mediaGols'] = jogador['totalGols'] / jogador['partidas']
    jogadores.append(jogador)
    print(f"{jogador['nome']} cadastrado com sucesso!")
    while True:
        opcao = str(input('Deseja cadastrar outro jogador? [S/N] ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Erro! Por favor digite S (sim) ou N (não)')
        else:
            break
    if opcao == 'N':
        break
print('-=' * 20)
print('FIM DO CADASTRO')
while True:
    print('-= JOGADORES CADASTRADOS =-')
    for i, jogador in enumerate(jogadores):
        print(f'{i:^2} {"." * 10} {jogador["nome"]}')
    selecao = int(input("Exibir detalhes de qual jogador? (999 para sair) "))
    if selecao == 999:
        break
    elif selecao >= len(jogadores):
        print(f'ERRO! Não há jogador na posição {selecao}')
        sleep(2)
    else:
        print(f'Detalhes do jogador {jogadores[selecao]["nome"]}:'.upper())
        print(f'Partidas jogadas: {jogadores[selecao]["partidas"]}')
        for j in range (1, jogadores[selecao]["partidas"] + 1):
            print(f'Partida {j}: {jogadores[selecao]["listaGols"][j - 1]} gol(s)')
        print(f'Total de gols: {jogadores[selecao]["totalGols"]}')
        print(f'Média de gols por partida: {jogadores[selecao]["mediaGols"]:.2}')
        sleep(2)
print("FIM")
