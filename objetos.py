#CLASES
#1ER Forma
class Usuario:
    nombre = 'Ever'

#Instancia de la clase va en minuscula
usuario = Usuario()
print(usuario.nombre)

#2DA Forma
class Usuario2:
    def __init__(self, nom, ape):
        self.nom = nom
        self.ape = ape
    
    def saludo(self):
        print("Mi nombre es: ", self.nom, self.ape)

#Herencia
class Admin(Usuario2):
    def saludoAdmin(self):
        print("Mi nombre es: ", self.nom, self.ape, "y soy Administrador.")


usuario2 = Usuario2('Jose', 'Lopez')
usuario3 = Usuario2('Dan', 'Pos')

usuario2.saludo()
usuario3.saludo()

admin = Admin('Ever', 'Cifuentes')
admin.saludo()
admin.saludoAdmin()

# print(usuario2.nom, usuario2.ape,
#       usuario3.nom, usuario3.ape)