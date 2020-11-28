# 1) Multiplicar dos numeros sin usar el simbolo de multiplicacion

def multiplicar(n1, n2):
    resultado = 0
    for x in range(n1):
        resultado += n2
        # return resultado
    print(resultado)
    
multiplicar(5,12)