
def es_numero_perfecto(numero):
    suma = 0
    
    for i in range(1, numero):
        if numero % i ==0:
            suma += i
            print(i, 'es numero perfecto')
        else:
            print(i, 'no es numero perfecto')    
    return suma == numero 


print(es_numero_perfecto(1))
print(es_numero_perfecto())  