# 5) Escribir una funcion que indique si el usuario es mayor de edad
def mayorEdad(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad
        
usuario1 = Usuario(14)
usuario2 = Usuario(30)

r1 = mayorEdad(usuario1)
r2 = mayorEdad(usuario2)

print(r1, r2)