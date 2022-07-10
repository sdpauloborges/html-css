import random

'''
input numero aleatorio
input chute Usuario
comparar chute com numero aleatorio
dizer se é menor ou maior ou igual
imprimir na tela
'''
aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('chute um numero de 1 a 10: '))
    if chute > aleatorio:
        print('chute maior que o numero, tente novamente')
    if chute < aleatorio:
        print('chute menor que o numero, tente novamente')
    if chute == aleatorio:
        acertou = True
        print('acertou')