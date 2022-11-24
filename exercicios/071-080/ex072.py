""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso """

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
japones = ('零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十')
while True:
    while True:
        escolhido = int(input('Digite um número de 0 a 20 para ver seu kanji em japonês: '))
        if 0 <= escolhido <= 20:
            break
        else:
            print('Número além do limite possível, tente novamente.')
    print(f'O número {extenso[escolhido]} é representado pelo kanji {japones[escolhido]}')
    opcao = str(input('Deseja tentar com outro número? [Digite N para sair] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('Até mais! またね！')
