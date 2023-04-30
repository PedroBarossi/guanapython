""" Faça um programa que tenha uma função notas() que pode receber várias notas de 
alunos e vai retornar um dicionário com as seguintes informações:
-Quantidade de notas
-A maior nota 
-A menor nota
-A média da turma
-A situação (opcional)   """

def notas(*nota, situacao=False):
    """
    -> Função para analisar as notas e situação de uma turma
    :param nota: aceita múltiplas notas
    :param situacao: opcional, adiciona a situação ao retorno
    :return: dicionário com diversas informações sobre a turma
    """
    retorno = {
        'quantidade': len(nota),
        'maior': 0,
        'menor': 0,
        'media': 0,
        'situacao': ''}
    soma = 0
    for n in range(0, len(nota)):
        soma += nota[n]
        if n == 0:
            retorno['maior'] = retorno['menor'] = nota[n]
        else:
            if retorno['maior'] < nota[n]:
                retorno['maior'] = nota[n]
            if retorno['menor'] > nota[n]:
                retorno['menor'] = nota[n]
    #Obs: esse trabalho todo acima poderia ter sido substituído
    #por max, min e sum :D
    retorno['media'] = soma / retorno['quantidade']
    if situacao:
        if retorno['media'] < 7:
            retorno['situacao'] = 'RUIM'
        elif retorno['media'] < 8:
            retorno['situacao'] = 'REGULAR'
        else:
            retorno['situacao'] = 'BOA'
    else:
        retorno.__delitem__('situacao')
    return retorno

print(notas(4, 5, 6, 6, situacao=True))
print(notas(8, 8.5, 10,))
print(notas(8, 8.5, 10, situacao=True))
print(notas(6, 9, 5.5, 7, 8, 6.5, situacao=True))
