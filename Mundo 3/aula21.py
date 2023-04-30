#help(print)
#print(input.__doc__)

def contador(i, f, p):
    """
        ->Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

#contador(2, 10, 2)

help(contador)

def soma(a, b, c=0): #atribuindo 0 como default, c vira um -parâmetro opcional-
#(todos poderiam ser opcionais)    
    s = a + b + c
    print(f'A soma vale {s}')

#Escopo de variáveis
def teste(b):
    #global n ->força a usar a variável global
    n = 5
    b += 4
    c = 2
    print(f'Na função: n = {n}, b = {b} e c = {c}')

n = 2
print(f'No programa principal, n vale {n}')
teste(n)
#print(c) ->não funciona porque c está fora do escopo global

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar(2, 3, 4)
r2 = somar(5, 7)
r3 = somar(10)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
