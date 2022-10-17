#Chefão 1
#Crie um script Python qye leia o nome de uma pessoa e mostre
#uma mensagem de boas-vindas de acordo com o valor digitado



nome = input("Digite seu nome: ")

if(nome == "Nathanson"):
    print("Get lost,", nome)
else:
    print("Seja bem-vindo(a),", nome)

#Chefão 2
#Crie um script Python que leia o dia, o mês e o ano de nascimento
#de uma pessoa e mostre uma mensagem com a data formatada
dia = input("Em que dia do mês você nasceu? ")
mes = input("Em que mês você nasceu? (1-12) ")
ano = input("Em que ano você nasceu? ")

print(nome, "nasceu na data", dia, "/", mes, "/", ano)

#Chefão 3
#Crie um script Python que leia dois números e tente mostrar
#a soma entre eles
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

print("A soma entre", numero1, "e", numero2, "é igual a", numero1+numero2)