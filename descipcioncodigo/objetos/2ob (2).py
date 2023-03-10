class Persona:# se crea una clase llamda usuario 
    def __init__(self,nombre):# se crea un funcion dentro de la calse usuario pero fuera es un metodo 
                              # init es como un iniciador 
        self.__nombre=nombre  # asigna nombre a __nombre para volverlo privado        
        #print('Constructor Activado')        
                              #self es una palabra reserva para indiacar que esos atributos perotenecen a la calse perosna 

    def getNombre(self):           #crea un funcion que despues va aser un metodo 
        return self.__nombre       # retorna el nombre pero solo el nombre 

    def setNombre(self,nombre):
        self.__nombre=nombre

ob=Persona('Maria')
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
#print(type(ob)) # hacer gtater y setree 
#agrgardocumento a persona 
#hacer un metodo para veer todos los datos en aprendiz