#condicionais
# if, elif, else
'''
cheguei atrasado posso entrar?
se eu nao for a terceira vez, pode, caso seja sera suspenso
'''

if int(numero_de_atrasos) >= 3:
numero_de_atrasos = input ("quantos atrasos? ")
    print('voce esta suspenso')
elif int(numero_de_atrasos) == 1:
    print('pode entrar')
elif int(numero_de_atrasos)1 == 2:
    print('pode entrar na proxima sera suspenso')
else:
    print('pode entrar')