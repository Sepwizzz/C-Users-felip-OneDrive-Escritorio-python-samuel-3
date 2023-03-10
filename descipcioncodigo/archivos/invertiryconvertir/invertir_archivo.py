from Aprendiz import *                                                # importa el archivo aprediz que dentro esta la clase arendiz que destro de se archivo tiene erencia de persona 
from Curso import *                                                   # importa el el archivo curso 

with open('invertiryconvertir/aprendices.txt','r') as flujo:          # se de calra un bloque de codigo with para si no preosuparse del cerrar 
                                                                      # ojo la letra que esta despues de la coma de la ubicacion del archivo indica lo que vamos a hacer  
    datos=flujo.read()                                                # almacena el flujo con el metodo leer en datos 
    print(datos)                                                      # imprime datos 
    #flujo.write('2560664,maria,123')
aprendices=[]                                                         # crea un lista llamada aprendices 
with open('invertiryconvertir/aprendices.txt','r') as flujo:          # se de calra un bloque de codigo with para si no preosuparse del cerra
    for linea in flujo:                                               # este for reccorre los datos linea por linea  del archivo  
        #print(linea)
        aprendices.append(linea.rsplit())                             # agrega linea a la lista aprendices pero quitando el salto de linea con el metodo rsplit 

datosxlinea=[]                                                        # crea lista datosxlinea
for aprendiz in aprendices:                                           # este for recorre la lista aprendices que los datos ficha,nombre y coumento pertenenec a una sola pocision
    datosxlinea.append(aprendiz[0].split(','))                        # agrega los datos que son dividos por el metodo split(",") qeu se spesifica una ,,


#print(ob.getNombre())

print(datosxlinea)                                                    # imprime la lista datosxlinea pero ahora ficha, nombre y documeto tiene du porpia pocicion en la lista ya no comparten solo una pocision

listaDeObjetos=[]                                                     # crea una lista llamada listaDeObjetos  

for apr in datosxlinea:                                               # este for recorre la lista datosxlinea pero por pocisiones
     f=apr[0]                                                         # de la linea 27 a la 29 guada variables con las tres pocisiones de la lista 
     n=apr[1]
     d=apr[2]
     ob=Aprendiz(f,n,d)                                               # crea un objeto de la calse aprendiz con las variables que estan en la linea 27 a la 29
                                                                      # que son ficha  nombre y documento 
     print(ob)                                                        # imprime el objeto de la clase aprendiz 
     listaDeObjetos.append(ob)                                        # agrega el objeto a la lista llamada listaDeObjetos

for xx in listaDeObjetos:                                             # este for recore la lista llamada listaDeObjetos con el xx 
    print(xx.getNombre())                                             # de la linea 36 ala 38 aca el xx llamada los metodos para que retorne los los datos del objeto 
    print(xx.getDocumento())
    print(xx.getFicha())