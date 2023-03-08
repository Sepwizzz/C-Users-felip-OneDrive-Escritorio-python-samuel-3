class pedido:
    def __init__(self,iduso):
        self.__id=iduso
        self.libros=[]
        print()

    def getpedido(self):
        id=self.__idusu
        tdm=self.__titulom
        #cm=self.__cogigom
        print("s codigo personal es:",id,"\nel titulo del libro es :",tdm,"\ncodigo correspondiente :")
    
    def agregarlibro(self,titulod,tipod,auto,editorial,codigolibro):#son 4 y me esta conatando el self
        self.__codigolibro=codigolibro
        self.__titulod=titulod
        self.__tipod=tipod
        self.__auto=auto
        self.__editorial=editorial
        self.libros.append(titulod)
        print(self.libros,"fue prestado a:", self.__id," el libro con el codigo :",self.__codigolibro)
       

class libro(pedido):
    def __init__(self,titulodl,tipodl,autor,editorisl,codigolibro):
        #super().__init__(titulodl,tipodl,autor,editorisl)
        self.__codigolibro=codigolibro
        self.__tipodl=tipodl
        self.__autor=autor
        self.__editorisl=editorisl
        self.__titulodl=titulodl
        self.__listl=[]

    def getlibro(self): 
        codigoo=self.__codigolibro
        tiulo=self.__titulodl
        tipo=self.__tipodl
        autor=self.__autor
        editorial=self.__editorisl
        print("el libro :",tiulo,"\ntipo de libro :",tipo,"\nel autor del libro :",autor,"\nsu editorial :",editorial,"su cofigo unico",codigoo)
        self.__listl.append(tiulo)
        #print(self.__listl)
        return self.__titulodl
    def agregarlibro(self,titulod,tipod,auto,editorial):
        #super().agregarlibro(titulod,tipod,auto,editorial)
        super().__init__(titulod,tipod,auto,editorial)

li=libro("ertor","musica","ector","pana bock",150)
li2=libro("manu y sus amigos ","comedia ","ector manuel", "colomnian bucks",8383)
#li.getlibro()
#li2.getlibro()
p1=pedido(123)
p1.agregarlibro("ertor","musica","ector","pana bock",150)
