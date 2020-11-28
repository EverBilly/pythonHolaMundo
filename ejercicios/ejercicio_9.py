# 9) Escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo
def agregar(nombre, apellido):
    archivo = open('nombres.txt', 'a')
    archivo.write(nombre + ' ' + apellido + '\n')
    archivo.close()
    
agregar('Ever', 'Cifuentes')