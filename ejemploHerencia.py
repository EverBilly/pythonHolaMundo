class Animal:
    def __init__(self, nombre, onomatopeya, edad):
        # self.tipoAnimal = tipoAnimal
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        self.edad = edad
    def saludo(self):
        print('Soy un', self.tipo, 'mi nombre es', self.nombre, 'mi sonido es el', self.onomatopeya, 'y mi edad es', self.edad, 'edad')

class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, onomatopeya, edad):
        Animal.__init__(self, nombre, onomatopeya, edad)
        print('Hola soy un gato extendido!')

class Perro(Animal):
    tipo = 'Perro'
    def __init__(self, nombre, onomatopeya, edad):
        super().__init__(nombre, onomatopeya, edad)
        print('Instanciando un perro!')

class Pato(Animal):
    tipo = 'Pato'
    
class Pollo(Animal):
    tipo = 'Pollo'


# animal = Animal('Fufy', 'Ladrido', 5)

gato = Gato('Luffy', 'maullido', 5)
gato.saludo()

perro = Perro('Oso', 'ladrido', 8)
perro.saludo()

pato = Pato('Any', 'gaznar', 3)
pato.saludo()

pollo = Pollo('Mr', 'Pio', 2)
pollo.saludo()