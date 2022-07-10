# coleções listas
preços = [20, 50, 200]
# indice   0   1   2
print(preços[1])
print(preços.index(200))

# lista
diversidades = [15, 'john', True]
for diversidade in diversidades:
    print(diversidade)

'''
exemplo 5
dados uma coleção de dados idades 15, 46, 75, 34, 23
imprima na tela a soma deste valores
'''
idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
print(total)