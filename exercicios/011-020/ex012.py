#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: R$'))
porcentagemDesconto = 5
precoComDesconto = preco - (preco * porcentagemDesconto / 100)
print('Um produto que custa R${:.2f}, com {}% de desconto, sai por R${:.2f}'.format(preco, porcentagemDesconto, precoComDesconto))
