#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Digite a temperatura em ºC: '))
fahren = celsius * 1.8 + 32
kelvin = celsius + 273
print('A temperatura de {:.1f}ºC equivale a {:.1f}ºF ou {:.1f}K'.format(celsius, fahren, kelvin))
