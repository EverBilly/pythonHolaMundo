#Importar Modulos
import modulos

print(modulos.mascotas)
modulos.saludo('Ever')

modulos.ingresaDatos("Juan", "Lopez", 25)

print('--------------------------------------------------')
#Importar Modulos y Renombrarlos
import modulos as mas

print(mas.mascotas)
mas.saludo('Ever')

print('--------------------------------------------------')
#Seleccionar lo importado
from modulos import saludo, mascotas

saludo('Cifuentes')

print('--------------------------------------------------')
from camelcase import CamelCase

c = CamelCase()
s = 'esta es una sentencia'
print (c.hump(s))