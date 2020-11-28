# 3) Escribir una funcion que encuentre el elemento menor en una lista
lista = [4,4,6,98,1]

menor = 0

for x in lista:
    if menor == 0:
        menor = x
    else:
        menor = x if x < menor else menor

print('Numero Menor:', menor)