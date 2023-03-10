class Aprendiz:  # crea la clase aprendiz 
    def __init__(self,nombre):  # constructor 
        self.__nombre=nombre    # guarda nombre 
        self.__cursos=[]        # crea euna lista 
    def agregarCurso(self,nombreCurso):# este metodo es para agregar cursos 
        self.__cursos.append(nombreCurso) # agrega los curso a cursos 
    
    def verCursos(self): # este para ver los cursos que furron al macenados en la lista cursos 
        return self.__cursos # retrona la lista de los curso que anteriuor mente fueron agregados 

class Curso:# calse curso ojo sin depencia 
    def __init__(self,nombreCurso):# constructro 
        self.__nombreCurso=nombreCurso# aca al macena el nuevo curso

    def getNombreCurso(self):  # este metodo es para ver curso agreagado 
        return self.__nombreCurso# muestra el curso agregado
    
ob=Aprendiz('Miguel') # se define el objeto ob()  como de la clase aprendiz 
c1=Curso('Python Basico') # c1 se define de la clase cursos 
c2=Curso('Python Intermedio')  # c2 se define de la clase cursos 
c3=Curso('Java Basico')# c3 se define de la clase cursos 

ob.agregarCurso(c1)# aca se reccacionan los objetso aunsiendo de otras clases que no tienen herencia 
ob.agregarCurso(c2)
ob.agregarCurso(c3)

for curso in ob.verCursos(): # curso recorrre vercurso
    print(curso.getNombreCurso())# aca enseñarael nombre del curso con el ghet nombre curso

del ob # elimina el objeto 
#print(ob)
print('.....',c1.getNombreCurso()) # imprime el curso por que no depende del aprendizn ese objeto se definio en la linea 19 como un objeto de curso  
