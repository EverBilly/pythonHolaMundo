# 7) Escribir una funcion que indique cuantas vocales tiene una palabra
def cuentaVocales(palabra):
    vocales = 0
    for x in palabra:
        y = x.lower()
        vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0
    return vocales
        
p = 'hosasupermayorAAAAEEEE'
print(cuentaVocales(p))
