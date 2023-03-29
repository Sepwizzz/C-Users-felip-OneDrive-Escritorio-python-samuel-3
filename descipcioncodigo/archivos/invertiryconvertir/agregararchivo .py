from Aprendiz import *                                                # importa el archivo aprendiz que dentro esta la clase aprendiz que destro de se archivo tiene herencia de persona 
from Curso import *                                                   # importa el el archivo curso 

nombre=input('ingrese nombre del aprendiz')                           # de la linea 4 a la 8 pide datos y los almacena en una variable 
documento=int(input('ingrese documento del aprendiz'))
ficha=input('ingrese ficha del aprendiz')
nombreCurso=input('ingrese nombre del curso')
horas=int(input('ingrese intensidad horaria del curso'))              #linea 8

ap=Aprendiz(ficha,nombre,documento)                                   # crea el objeto aprendiz con las variables que estan en desde la linea 4 a la 6  como atributos 
                                                                      


c1=Curso(nombreCurso,horas)                                           # crea un objeto con la variables de la linea 7 y 8 como atrivutos para el objeto 

ap.agregarCurso(c1)                                                   # agrega el curso c1 a aprendiz con el metodo agregarCurso

with open('invertiryconvertir/aprendices.txt','w') as flujo:          # se de clara un bloque de codigo with para si no preosuparse del cerrar
                                                                      # ojo la letra que esta despues de la coma de la ubicacion del archivo indica lo que vamos a hacer  
                                                                      # se da la ubicacion del archivo al cual seva a agregar invertiryconvertir/aprendices.txt' y lo convierte en flujo  
    
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')# aca llama los metodos de la clase aprendiz que los que son getNombre,getDocumento son metodos de la clase persona 
                                                                                 # su funcion es retornar los datos agregados y todo se vuelve una cadena y se corviertye en una sola cadena gracias al +
                                                                                 # despues pone las ,, como pades de divicion para poder ditringir o como en el siguente archivo invertir_archivo.py inviete y los vuelve a agregar gracias la ,,
