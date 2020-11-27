palabra = 'Hola Mundo' #STRING
oracion = "Hola Mundo 2" #STRING

entero = 10 #INTEGER
float1 = 20.4 #FLOAT
complejo = 2j

#print(palabra, oracion, entero, float1, complejo)

#LISTAS -> COLECCION DE DATOS
lista = [1,2,3]
lista2 = lista.copy()
#agregar registros a la lista
lista.append(4)

# lista.clear()
print(lista, lista2)
# contar numero veces se repite un numero
print(lista2.count(2))
print('Longitud Lista 1: ', len(lista), 'Longitud Lista 2: ', len(lista2))
print(lista[0])

#eliminar el ultimo registro de la lista
lista.pop()
print(lista)

#eliminar elemento especifico de la lista
lista.remove(2)
print(lista)

#ordena la lista del ultimo al primer dato
lista.reverse()
print(lista)

#ordena la lista del primer al ultimo dato del mismo tipo de datos
lista.sort()
print(lista)

#-------------------------------------------------------------------------------------
#TUPLAS
#Las tuplas no son modificables
tupla = ('hola', 'mundo', 'somos', 'tupla')
print('Tupla: ', tupla.count('hola'))
print('Tupla: ', tupla.count('hola'))
print('Tupla: ', tupla[2])

#Convertir una tupla a lista
listaDeTupla = list(tupla)
listaDeTupla.append('nuevo')
print(listaDeTupla)

rango = range(6)
print(rango)

diccionario = {
    "nombre" : "oso",
    "raza" : "pastor aleman",
    "edad" : 5
}

#Copiar Diccionario
copiaDiccionario = diccionario.copy()

#Otra Forma de copiar Diccionario
copiaDiccionario2 = dict(diccionario)

print(diccionario)
print(diccionario['raza'])
print(diccionario.get('nombre'))

#Cambiar valor a campo de diccionario
diccionario['nombre'] = 'Chuky'
print(diccionario, 'Longitud Diccionario: ', len(diccionario))

#Agregar datos al diccionario
diccionario['Cuida Casa'] = 'Si'
print(diccionario)

#Eliminar de un diccionario
diccionario.pop('edad')
print(diccionario)

#Elimina el ultimo valor que se agrego al diccionario
diccionario.popitem ()
print(diccionario)

del diccionario['nombre']
print(diccionario, copiaDiccionario)
print(copiaDiccionario2)

#Diccionario Anidado
#Forma 1
print("Anidacion de Diccionarios")
perros = {
    'Lord': {
        'nombre' : 'Lord P',
        'edad' : 3
    },
    'Ornato' : {
        'nombre' : 'Ornato Oso',
        'edad' : 5
    }
}
print("Perros: ", perros)

#Diccionario Anidado
#Forma 2
lord = {
    'nombre': 'Lord P',
    'edad': 3
}
ornato = {
    'nombre': 'Ornato Oso',
    'edad': 5
}

perros2 = {
    'perro_1': lord,
    'perro_2': ornato
}
print(perros2)

#Diccionario 
#Forma 3
perros3 = dict(nombre= 'Sabueso', edad= 5)
print('Perros 3: ', perros3)

verdadero = True
falso = False
print(verdadero, falso)