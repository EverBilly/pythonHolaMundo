print('----------------------------------------------------------------------')
leer = open('archivo.txt')
# lineas = leer.readlines()
try:
    for lee in leer.readlines():
        print(lee)
    pass
finally: 
    leer.close()