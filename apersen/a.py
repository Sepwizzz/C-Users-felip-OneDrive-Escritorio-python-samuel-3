class producto:                                             #creop la clase producto 
    contador=0                                              #conator en cero para despues saber cuantos productos hay 
    def __init__(self,nombre,precio):                       # el init con dos parametros en la funcion 
        self.__nombre=nombre                                # linea 4 y 5 guardo nombre y precio delmproducto 
        self.__precio=precio
        #print(producto.contado)
        producto.contador+=1

    def getproducto(self):                                 # de la linea 9 a la 11+2  son metodos para que me devuelvan el nombre y el valor 
        return self.__nombre
    
    def getprecio(self):
        return self.__precio
    
    def seterprecio(self,precio):                                                 # este metodo es para modificar el precio 
        precio1=self.__precio                                                     # linea 16 y 17 declaro nombre y precio antiguo en un valiable 
        nombre2=self.__nombre                                                     #para imprimir en la linea 18
        print("usted esta modificando el precio de",nombre2 ,"que es:",precio1,)
        
        self.__precio=precio                                                      # aca guado el nuevo precio 
        print("al siguente",self.__precio)                                        # y aca imprimo el nuevo precio 
        #return self.__precio       
    
               
    def seterproducto(self,nombre):                                               # metodo para cambiar el nombre el producto 
        self.__nombre=nombre
        return self.__producto
    

    def cuntoiva(self):                                                 # linea 30 a la 35 metodo para saber le iva 
        
        print("cunato iva por el producto")
        i=self.__precio*0.19
        p=self.__nombre
        print(p,"su iva es de :",i)
         
# de la linea 37 a la 50 declaro productos y utlizo los metodos 
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


with open('apersen/productos.txt','w') as flujo:          # se de calra un bloque de codigo with para si no preosuparse del cerrar
                                                                      # ojo la letra que esta despues de la coma de la ubicacion del archivo indica lo que vamos a hacer  
                                                                      # se da la ubicacion del archivo al cual seva a agregar 'apersen/productos.txt' y lo convierte en flujo  
    
    flujo.write (p.getproducto()+","+str(p.getprecio()) +"\n"+a.getproducto()+","+str(a.getprecio()) +"\n")# aca llama los metodos de la clase producto que los que son getproducto() y getprecio() son metodos de la clase porducto
                                                                                 # su funcion es retornar los datos agregados y todo se convierte en una cadena y se corviertye en una sola cadena gracias al +
                                                                                 # despues pone las ,, como paredes de divicion para poder ditringir  como una casilla de ecxel 


