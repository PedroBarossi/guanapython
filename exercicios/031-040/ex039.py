#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
#tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

atual = date.today()
nasc = int(input('Informe seu ano de nascimento: '))
sexo = int(input('Digite seu sexo (1-Masculino; 2-Feminino): '))
if sexo != 1:
    print('Seu alistamento não é obrigatório')
else:
    idade = atual.year - nasc
    if idade < 18:
        print('Ainda falta(m) {} ano(s) para você se alistar.'.format(18 - idade))
        print('Você vai se alistar no ano {}.'.format(atual.year + (18-idade)))
    elif idade > 18:
        print('Você deveria ter se alistado há {} ano(s).'.format(idade - 18))
        print('Seu ano de alistamento foi {}.'.format(atual.year - (idade - 18)))
    else:
        print('Você está no ano de se alistar!')
