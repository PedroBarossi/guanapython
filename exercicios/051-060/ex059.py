""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso """
opcao = 0
while opcao != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    opcao = int(input("""Selecione a operação:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Alterar os números
[5] Sair do programa
"""))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} X {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 < n2:
            print('O maior dos valores é {}'.format(n2))
        elif n1 > n2:
            print('O maior dos valores é {}'.format(n1))
        else:
            print('Os dois valores são iguais')
    elif opcao == 4:
        print('Voltando ao início...')
    elif opcao > 5:
        print('Opção inválida')
print('Tchauzinho!')

#Dessa maneira, o programa sempre lerá dois números, diferente da resposta do vídeo