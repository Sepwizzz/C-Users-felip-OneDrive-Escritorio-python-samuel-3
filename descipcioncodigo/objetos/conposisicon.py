class Curso:                             #calse curso 
    def __init__(self,titulo):# constructor
        self.__titulo=titulo # guardda el curso

    def getTitulo(self):    #2 metodod que me develve el curso 
        return self.__titulo

class Aprendiz:    # clase aprendiz 
    def __init__(self,nombre):# constructro 
        self.__nombre=nombre  # nombre lo guarda 
        self.__cursos=[] # una lsita llamada cursos 

    def agregarCurso(self,nombreCursito):# 
        cursito=Curso(nombreCursito)     #curso lo guarda en curso cursito
        self.__cursos.append(cursito)    # agrea cursito en lista de curso qu esta en el init de esta clase 

    def getCursos(self):  # metodo que retorna los cursos que se agregaron a la lista osea retrona la lista
        return self.__cursos
    
ap=Aprendiz('Sofia')# crea objeto  DE APRWNDIZ 
ap.agregarCurso('Python Basico')        #y al objeto se le agreaga  el objeto aprendiz osea para  lo manipule pero distito como el de agregacion en un objeto pero aca no esta definido 
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())

del ap