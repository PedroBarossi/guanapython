#Erro de sintaxe

#primt(x) ->Comando escrito errado

#Erro semântico

#print(x) ->Variável não inicializada

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Infelizmente, houve um problema com o tipo dos dados :(')
except ZeroDivisionError:
    print('Impossível dividir por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro: #genérico
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre.')
