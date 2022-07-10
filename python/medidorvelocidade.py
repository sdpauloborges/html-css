
'''
velocidade_maxima = 80
input velocidade
comparar vpermitida com vusuario
exibir se levou multa
'''

vmaxima = 80
vusuario = int(input('digite a velocidade? '))
if vusuario <= vmaxima:
    print('nao levou mnulta')
elif vusuario > vmaxima and vusuario <= vmaxima + 10:
    print('levou multa leve')
elif vusuario >= vmaxima + 11 and vusuario <= vmaxima + 20:
    print('levou multa grave')
elif vusuario > vmaxima + 20:
    print('levou multa gravissima')

