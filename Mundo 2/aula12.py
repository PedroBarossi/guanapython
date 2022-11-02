nome = str(input('Qual é seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'João' or nome == "Maria":
    print('Seu nome é bastante popular!')
elif nome in 'Deborah Monica Jennifer':
    print('Você tem o nome de uma bela atriz!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
