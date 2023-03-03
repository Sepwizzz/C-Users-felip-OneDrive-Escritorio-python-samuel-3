class producto:
    contador=0
    def __init__(self,nombre,precio):
        
        self.__nombre=nombre
        self.__precio=precio
        #print(producto.contado)
        producto.contador+=1

                
    def getproducto(self):
        return self.__nombre
    
    def getprecio(self):
        return self.__precio
    
    def seterprecio(self,precio):
        precio1=self.__precio
        nombre2=self.__nombre
        print("usted esta modificando el precio de",nombre2 ,"que es:",precio1,)
        
        self.__precio=precio
        print("al siguente",self.__precio)
        #return self.__precio       
    
               
    def seterproducto(self,nombre):
        self.__nombre=nombre
        return self.__producto
    

    def cuntoiva(self):
        
        print("cunato iva por el producto")
        i=self.__precio*0.19
        p=self.__nombre
        print(p,"su iva es de :",i)
        

    
p=producto("TV Samsung FLAT LED Smart 32”HD",800900)
a=producto("xbox series s",1599900)
print()
print(p.getproducto(),":",p.getprecio())
print()
p.seterprecio(900900)
print()
p.cuntoiva()
print()
print(a.getproducto(),":",a.getprecio())
a.cuntoiva()
print()

print("veces utilizada:",producto.contador)



