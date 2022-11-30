""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. """

expressao = str(input('Infrome uma expressão algébrica: ')).strip()
abre = fecha = 0
for c in expressao:
    if c == '(':
        abre += 1
    if c == ')':
        fecha += 1
    if fecha > abre:
        print(f'A expressão {expressao} é inválida')
        break
if abre == fecha:
    print(f'A expressão {expressao} é válida')
elif abre > fecha:
    print(f'A expressão {expressao} é inválida')

#Solução Guanabara
""" pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'A expressão {expressao} é válida')
else:
    print(f'A expressão {expressao} é inválida') """