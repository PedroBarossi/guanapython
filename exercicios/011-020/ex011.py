#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
print('Sua parede tem as dimensões {}x{}'.format(largura, altura))
print('Para pintar uma parede de área {}m², serão gastos {}l de tinta'.format(area, area /2))
