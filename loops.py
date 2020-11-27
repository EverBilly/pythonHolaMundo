i = 0
while i < 5:
    print(i)
    i += 1

h = 0
while h < 5:
    h += 1
    if h == 3:
        continue
    print(h)

#Recorrer Lista
usuarios = ['Jan', 'Quetzali', 'Mario', 'Marcos', 'Arana']

for usuario in usuarios:
    print(usuario)

#Recorrer String
user = 'Chanchito Feliz'

for j in user:
    print(j)

#Break
nombres = usuarios

for nombre in nombres:
    if nombre == 'Mario':
        break
    print(nombre)

#Continue
nombres1 = nombres

for nombre1 in nombres1:
    if nombre1 == 'Mario':
        continue
    print(nombre1)

#Range con For
for x in range(1, 7):
    print(x)

#Aumentar Valor de tanto en tanto
for m in range(1, 20, 2):
    print('Aumento de 2: ', m)
else: 
    print('Hemos Terminado!!')