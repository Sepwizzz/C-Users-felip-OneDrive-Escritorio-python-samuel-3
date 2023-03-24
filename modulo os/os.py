import os  # esprarecido al phat  

#------ saber ubicaion ubicacion y esatr dentro 
"""
print(os.getcwd()) # este meytodo de os es para ser la ruta de donde estoy ubicado 

print(os.path.abspath("hola")) #este para saber la ruta de un archoivo o carpeta 

os.chdir("buenas noches") #con este metodo me ubico endentro de una carpeta
"""
#------------para saber el contenido de un archivo
"""
print(os.listdir()) # para listar todo lo que tengo en la carpeta en la que estoy ubicado 
print(os.listdir("hola")) #dentro de los parentecis se puede colocar el nombre de la carpeta la cual se quiere ver su contenido 
"""
#-----para crear 

"""
os.mkdir("buenas noches") # con este metodo mrditr se puede crear una nueva carpeta 
print(os.listdir())
"""
"""
os.makedirs("buenas noches/buenos dias") # con este metodo puedo crear una carpeta dentro de otra espesificando la ruta 
print(os.listdir("buenas noches"))
"""
"""
os.chdir("buenas noches") #con este metodo me ubico endentro de una carpeta para mostar el contenido
print(os.listdir())
"""

#------aca crear y eliminar 

"""
os.mkdir("hola2")   # aca creo la carpeta hola 2
print(os.listdir()) # para ver que se creo 

os.rmdir("hola2") # y aca con el metodo rmdir boro la carpeta hola2
print(os.listdir()) # para ver que la borro 
"""

"""
os.makedirs("buenas noches/buenos dias") # igual para crear un carpeta dento de esa carpeta 
os.removedirs("buenas noches/buenos dias/buneas tardes") #aca elimino la carpeta inicial como su contenido espesificando 
os.chdir("buenas noches")  
print(os.listdir())
"""


os.mkdir("C:/buenas noches/buenos dias")
