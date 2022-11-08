""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos """
somaIdades = 0
maisVelhoIdade = 0
maisVelhoNome = ''
mulheresSub20 = 0
for pessoas in range(1,5):
    print('{}ª PESSOA:'.format(pessoas))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = int(input('Sexo (1 = Masc 2 = Fem): '))
    somaIdades += idade
    if (sexo == 1) and (idade > maisVelhoIdade):
        maisVelhoIdade = idade
        maisVelhoNome = nome
    if (sexo == 2) and (idade < 20):
        mulheresSub20 += 1

print('Média das idades: {:.1f}'.format(somaIdades / 4))
if maisVelhoNome == '':
    print('Nenhum homem estava entre os informados')
else:
    print('Nome do homem mais velho: {}'.format(maisVelhoNome))
print('Mulheres abaixo de 20 anos: {}'.format(mulheresSub20))
