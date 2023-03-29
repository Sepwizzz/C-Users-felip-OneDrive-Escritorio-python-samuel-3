#print(type(ob)) # hacer gtater y setree 
#agrgardocumento a persona 
#hacer un metodo para veer todos los datos en aprendiz

class Persona:
    cedu3=int
    def __init__(self,nombre,tipo,cedu):
        self.__nombre1=nombre
        self.__tipo1=tipo
        self.__cedu1=cedu
        

        #print('Constructor Activado')        
    def getNombre(self):
        t=self.__tipo1
        c=self.__cedu1
        n=self.__nombre1
        print(n,t,c)
        
        

    def setNombre(self,nombre,tipo,cedu):
        self.__nombre1=nombre
        self.__tipo1=tipo
        self.__cedu1=cedu

   

ob=Persona('Maria',"cc",123)
ob.getNombre()
ob.setNombre('Ana',"ti",133)
ob.getNombre()
#print(type(ob))
print()

class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        self.__nombre1=nombre
        self.__ficha=ficha
        super()

    def getFicha(self,):
        #print("dentro de get")
        

        nombre1=self.__nombre1
        #tipo=self.__tipo1
        #cedu=self.__cedu1
        #ficha=self.__ficha
        self.__ficha
        

        #print("dentro de get")
        print(nombre1,self.__ficha,self.__)
        
    
    def setficha(self,nombre,ficha):
        ficha2=self.__ficha
        print(nombre,"cambio de numero de ficha que era", ficha2,"a la siguente",ficha)
        self.__nombre1=nombre
        self.__ficha=ficha
        sena="gracias por estar en el sena "
        return sena
        #print("2")
    
    def verap(self):
        return Aprendiz.self
    
 
      

app=Aprendiz("Ana","12345A")
app.getFicha()


print(app.setficha("Ana","12345b"))


