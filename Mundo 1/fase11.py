""" STYLE
0 none
1 bold
4 underline
7 negative """

""" TEXT
30 white
31 red
32 green
33 yellow
34 blue
35 purple
36 cyan
37 grey """

""" BACK
40 - 47
 """

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[4;33;44mOlá, Mundo!\033[m')
print('\033[1;35;43mOlá, Mundo!\033[m')
print('\033[30;42mOlá, Mundo!\033[m')
print('\033[mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[31m{} \033[me \033[34m{}'.format(a, b))
