""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros """

preco = float(input('Informe o preço do produto: R$'))
print('Selecione a forma de pagamento:')
pgto = int(input('[1]-Dinheiro à vista [2]-Cheque à vista [3]-Cartão\n'))
if pgto == 1:
    print('À vista no dinheiro, o produto tem 10% de desconto.')
    print('De R${:.2f} passa para R${:.2f}'.format(preco, preco - (preco * .1)))
elif pgto == 2:
    print('À vista no cheque, o produto tem 10% de desconto.')
    print('De R${:.2f} passa para R${:.2f}'.format(preco, preco - (preco * .1)))
elif pgto == 3:
    parcelas = int(input('Quer dividir em quantas parcelas? (Digite 1 para à vista no cartão)\n'))
    if parcelas == 1:
       print('À vista no cartão, o produto tem 5% de desconto.')
       print('De R${:.2f} passa para R${:.2f}'.format(preco, preco - (preco * .05)))
    elif parcelas == 2:
        print('Em 2 vezes no cartão, não há desconto ou juros.')
        print('2 parcelas de R${:.2f}\nTotal: R${:.2f}'.format(preco / 2, preco))
    else:
        print('Em {} vezes no cartão, há 20% de juros'.format(parcelas))
        comjuros = preco + (preco * .2)

        print('{} parcelas de R${:.2f}\nTotal: R${:.2f}'.format(parcelas, comjuros / parcelas, comjuros))
else:
    print('Opção inválida, operação cancelada')
