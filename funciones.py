#Funciones
def miFuncion():
    print('Primer Funcion!!!')

miFuncion()

def parametros(nombre, apellido):
    print("El nombre Completo es: ", nombre, apellido)

parametros('Ever', 'Cifuentes')

#Pasar N Argumentos
def nArgumentos(*nombre):
    print('El nombre es: ', nombre[1])

nArgumentos('Yo', 'Soy', 25)

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre='Edo', apellido='Tensei')

def nombreCompleto2(**kwargs):
    print(kwargs['name'], kwargs['apel'], kwargs['edad'])

nombreCompleto2(name='Di mi', apel='nombre', edad=25)

def miFuncion2(ape = 'Chancho'):
    print(ape)
miFuncion2('Love')
miFuncion2()

#Funcion Con Lista
def funcionLista(p):
    for m in p:
        print(m)
funcionLista(['Hola', 'Hacer'])

#Funcion Retorna Datos
def concatenaNombres(lista):
    i = ''
    for l in lista:
        i = i + l + ' '
    return i

names = concatenaNombres(['Pablo', 'Menos', '35'])
print(names)

def recursion(i):
    if i < 1:
        return i
    print(i)
    recursion(i - 1)

recursion(7)