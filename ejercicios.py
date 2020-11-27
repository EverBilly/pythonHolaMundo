# dato = input('Ingrese un dato: ')
lista = [ 'dinero', '$2,000.00', 'mensualmente', 'forex', 'programacion']

# if lista.count(dato) > 0:
#     print('El dato existe: ', dato)
# else: print('El dato no existe: :( ', dato)


primero = input('Ingresa el primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'cadena'
    if primero == 'cadena':
        print('Ha introducido mal un dato')
        exit()

segundo = input('Ingrese el segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'cadena'
    if segundo == 'cadena':
        print('Ha introducido mal un dato')
        exit()
operacion = input('Ingrese el operador: ')
if operacion == '+':
    print(primero + segundo)
elif operacion == '-':
    print(primero - segundo)
elif operacion == '*':
    print(primero * segundo)
elif operacion == '/':
    print(primero / segundo)
else: print('Operacion no valida')