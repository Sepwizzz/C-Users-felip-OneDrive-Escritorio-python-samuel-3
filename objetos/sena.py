#print(type(ob)) # hacer gtater y setree 
#agrgardocumento a persona 
#hacer un metodo para veer todos los datos en aprendiz

class Persona:
    def __init__(self,nombre,cc):
        self.__nombre=nombre,cc
        

        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre,cc):
        self.__nombre=nombre,cc

ob=Persona('Maria',123)
print(ob.getNombre())
ob.setNombre('Ana',133)
print(ob.getNombre())
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,cc,ficha):
        Persona.__init__(self,nombre,cc)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha
    
    def verap(self):
        return

app=Aprendiz('Pedro',55,12345)
#print(app.getFicha())
#print(app.getNombre())
print(app.verap)
