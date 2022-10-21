#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

COTACAO_DOLAR = 5.22 #22/10/2022
COTACAO_EURO = 5.12 #22/10/2022
COTACAO_IENE = 0.035 #22/10/2022
reais = float(input('Digite a quantidade em reais para converter em dólar: '))
dolares = reais / COTACAO_DOLAR
euros = reais / COTACAO_EURO
ienes = reais / COTACAO_IENE
print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, dolares))
print('Outras possibilidades são €{:.2f} e ¥{:.2f}'.format(euros, ienes))
