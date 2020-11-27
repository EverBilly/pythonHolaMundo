print('----------------------------------------------------------------------')
#Numeros Primos
def es_primo(numero):
    for num in range(2, numero):
        if numero%num == 0:
            print('No es primo', num, 'es divisor')
            return
    print('Es primo')
            
es_primo(13)