flujo=open('archivos/inicio.txt','a')  # declara una variable flujo despues del igual dice open eque es para que habra un archivo en espesifco 
                                       # se pone de argumento de segundo argumento que se quiere hacer en el archivo si leer,actualizar,escribir y  tambien el tipo de archivo por ejemplo binario o de texto 
                                
#datos=flujo.read()                    # aca guarda el flujo en datos y utiliza el metodo read()

#print(datos)                          # imprime datos osea lo que tine el archivo de la ruta de la niea 1 de estsa hoja 

flujo.write('\nCuando estudian con juicio')  # para escribir y actualizar el archivo 
datos=flujo.read()                           # lee el archivo dado 
print(datos)                                 # imprime  datos de la linea 9 


# funciona igual que los objetos se dan rutas para un archivo despues se puede edidar, leer o escribir con metodos
