class pedido:
    def __init__(self,iduso):
        self.__id=iduso
       
        print()
        self.libros=[]

    def getpedido(self):
        id=self.__idusu
        tdm=self.__titulom
        #cm=self.__cogigom
        print("s codigo personal es:",id,"\nel titulo del libro es :",tdm,"\ncodigo correspondiente :")
    
    def agregarlibro(self,titulod,tipod,auto,editorial,codigolibro):#son 4 y me esta conatando el self
        
         
        self.libros=[]
        self.__codigolibro=codigolibro
        self.__titulod=titulod
        self.__tipod=tipod
        self.__auto=auto
        self.__editorial=editorial
        self.libros.append(titulod)
        print(self.libros,"fue prestado a:", self.__id," el libro con el codigo :",self.__codigolibro)
       


#li=libro("ertor","musica","ector","pana bock",150)
#li2=material("manu y sus amigos ","comedia ","ector manuel", "colomnian bucks",8383)
#li.getlibro()
#li2.getlibro()
#p1=pedido(10199)
#p1.agregarlibro("ertor","musica","ector","pana bock",150)

class libros(pedido):
    def __init__(self,titulodl,tipodl,autor,editorisl,codigolibro):
        self.__codigolibro=codigolibro
        self.__tipodl=tipodl
        self.__autorr=autor
        self.__editorisl=editorisl
        self.__titulodl=titulodl
        self.__listl=[]
    def verlibro(self,titulodl,tipodl,autor,editorisl,codigolibro):
        codl=self.__codigolibro
        tipol=self.__tipodl
        autor=self.__autorr
        edito=self.__editorisl
        T=self.__titulodl
        print("el libro es : ",T,"el tipo de libro es :",tipol,"su codigo corespondiente es :",codl," su autor :",autor," su editorial :",edito)
    def setlibro(self,titulodl):
        edin=titulodl
        self.__titulodl=titulodl
        print("nombre a cambiar :",edin,"usted cambio su nombre a ",self.__titulodl)
        
        
class revista(pedido):
    def __init__(self,titulodl,tipodl,autor,edicion,codigolibro):
        self.__codigolibro=codigolibro
        self.__tipodl=tipodl
        self.__autorr=autor
        self.__editorisl=edicion
        self.__titulodl=titulodl
        self.__listl=[]
    def verrevista(self):
        codl=self.__codigolibro
        tipol=self.__tipodl
        autorr=self.__autorr
        edito=self.__editorisl
        T=self.__titulodl
        print("el libro es : ",T,"el tipo de libro es :",tipol,"su codigo corespondiente es :",codl," su autor :",autorr," su editorial :",edito)
    def setrevista(self,titulodl):
        edin=titulodl
        self.__titulodl=titulodl
        print("nombre a cambiar :",edin,"usted cambio su nombre a :",self.__titulodl)
        
        
ob=pedido(119982800)
pl=libros("ertor","musica","ector","panama bock",150)
rv=revista("manu y sus amigos ","comedia ","ector manuel", "semana",8383)



ob.agregarlibro("manu y sus amigos ","comedia ","ector manuel", "semana",8383)
        
        