
#ob2.getpedido() 
#print(ob2.setordeon("malono y sus amigos "))
#ob2.getpedido() 
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


#li=libro("ertor la voz","musica","ector","pana bock",150)
#li2=libro("manu y sus amigos ","comedia ","ector manuel", "colomnian bucks",8383)
#li.getlibro()
#print()
#li2.getlibro()
#p1=pedido(123)
#p1.agregarlibro("ertor la voz","musica","ector","pana bock",150)
"""
class revsita(pedido):
    def __init__(self,titulor,tipor,autorr,edicion):
        self.__titulor=titulor
        self.__tipor=tipor
        self.__autorr=autorr
        self.__edicion=edicion
        #super().getpedido()

    def getprevist(self):
        ti=self.__titulor
"""
class lector :
    def __init__(self,nombre,direcion,telefono):
        self.__nombre=nombre
        self.__direcion=direcion
        self.__telefono=telefono
        self.__listadl=[]

    def verlec(self):
        nom=self.__nombre
        diet=self.__direcion
        tele=self.__telefono
        print("\n su numbre es:" ,nom,"\n usted vive en :", diet,"\n su telefofno es :",tele)
        print(" gracias por pertenecer a nuestar biblioteca")
    
    def agregel(self,libro):
        self.__listadl.append(libro)
        print(self.__listadl)
    
    def moddi(self,direct):
        directa=self.__direcion
        self.__direcion=direct
        print(" usted acaba de modificar su direcion de :",directa,"\n a ala siguente:",self.__direcion)
        

    def telmodi(self,nomerot):
        nt=self.__telefono
        self.__telefono=nomerot
        print(" su numero antiguo es es:",nt,"usted tiene este nuevo numero",self.__telefono)


        
ob1=lector("manolo","calle11",310)  


libro12=("manolo y sus amigoa")
ob1.verlec()
print()
ob1.agregel("manolo y sus amigos")
print()
ob1.moddi("calle 10")
print()
ob1.telmodi(122)

class estudiante(lector):
    def __init__(self,codigoes):
        self.__cestudi=codigoes

        
    def getestu(self):
        return self.__cestudi
    
    def modicestu(self,codigo):
        codianti = self.__cestudi
        self.__cestudi=codigo
        print(" condigo antiguo",codianti,"\n nuevo codigo :",self.__cestudi)


class docente(lector):
    def __init__(self,codigoes):
        self.__cestudi=codigoes

        
    def getdoce(self):
        return self.__cestudi
    
    def modidoce(self,codigo):
        codianti = self.__cestudi
        self.__cestudi=codigo
        print(" condigo antiguo",codianti,"\n nuevo codigo :",self.__cestudi)


        tipO=self.__tipor
        au=self.__autorr
        edi=self.__edicion
        print("la revista :",tipO,"\ntipo de revista :",tipO,"\nel autor del libro :",au,"\nsu editorial :",edi)
        #super().__init__(self)
       
    def setordeon(sefl,titulolibro):

        sefl.__titulom=titulolibro
        super().setordeon(titulolibro)
        #return sefl.__titulom
        return super().setordeon(sefl.__titulom)

       
