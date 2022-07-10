# fatorial de um numero
'''
crei um programa que recebe um numero e imprime o fatorial daquele numero
# metodo 5Q's para montar um algoritimo?
analise criticamente o problema e descubra:
tente explicar este problema para voce mesmo em voz alta e peça mais informações investigue mais até você compreender completamente o problema 

1 quais sao os dados de entrada necessários
    numero
2 o que devo fazer com estes dados 
    calcular o fatorial e exibir na tela
3 quais sao as restrições deste problema
    deve ser positivo e inteiro
4 qual é o resultado esperado
    fatorial calculado e exibido
5 qual é a sequencia de passos a ser feita para chegar ao resultado esperado 
    input numero
    if numero > 0
    if numero = inteiro
    fatorial = 1
    loop de 1 ate numero
        fatorial = fatorial * numero
        print fatorial
'''
numero = int(input('diga um numero: '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print(fatorial)