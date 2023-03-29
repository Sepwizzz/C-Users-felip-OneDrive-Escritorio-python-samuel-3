
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
    def getNombre(self):
        return self.__nombre


"""     
ob1=lector("manolo","calle11",310)  


libro12=("manolo y sus amigoa")
ob1.verlec()
print()
ob1.agregel("manolo y sus amigos")
print()
ob1.moddi("calle 10")
print()
ob1.telmodi(122)
"""

class estudiante(lector):
    def __init__(self,nombre,direcion,telefono,codigoes):
        lector.__init__(self,nombre,direcion,telefono)
        self.__cestudi=codigoes
        
    # def verlec(self):
    #     return self.__nombre
    #     
        
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
       
    def setordeon(self,titulolibro):

        self.__titulom=titulolibro
        super().setordeon(titulolibro)
        #return sefl.__titulom
        return super().setordeon(self.__titulom)


def Biblioteca (var):
    print('1- Crear')
    print('2- Consulatr')
    while True:
        ctrl=str (input("Seleciona una opcion: "))
        match ctrl:
            case '1':
                print()
                print('1- crear estudiante')
                print('2- crear Docente')
                print('3-Crear libro')
                print('4-Crear revista')
                print('5-Crear bibliotecario')
                ctrl2=str (input("Seleciona una opcion: "))
                match ctrl2:
                    case '1':
                        c1=str(input('Nombre del estudiante: '))
                        c2=str(input('Dirección del estudiante: '))
                        c3=str(input('Telefono del estudiante: '))
                        c4=str(input('id del estudiante: '))
                        var=estudiante(c1,c2,c3,c4)
                    case '2':
                        c1=str(input('Nombre del Docente: '))
                        c2=str(input('Dirección del Docente: '))
                        c3=str(input('Telefono del Docente: '))
                        var=docente(c1,c2,c3)
                    case '3':
                        c1=str(input('Nombre del biblo: '))
                        c2=str(input('Dirección del Docente: '))
                        c3=str(input('Telefono del Docente: '))
                        var=(c1,c2,c3)
            case '2':
                print()
                print('1-ver estudiante')
                print('2- ver Docente')
                print('3- ver libro')
                print('4- ver revista')
                print('5- ver bibliotecario')
                ctrl3=str (input("Seleciona una opcion: "))
                match ctrl3:
                    case '1':
                        var.verlec()
                    case '2':
                        pass
                    case '3':
                        pass
                
            case '3':
                break
            
        

c=""
Biblioteca(c)
    

