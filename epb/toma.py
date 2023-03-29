"""
def Biblioteca (var):
    print('1- Crear')
    var=0
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
                        var=Estudiante(c1,c2,c3)
                    case '2':
                        c1=str(input('Nombre del Docente: '))
                        c2=str(input('Dirección del Docente: '))
                        c3=str(input('Telefono del Docente: '))
                        var=Estudiante(c1,c2,c3)
                    case '3':
                        c1=str(input('Nombre del Docente: '))
                        c2=str(input('Dirección del Docente: '))
                        c3=str(input('Telefono del Docente: '))
                        var=Estudiante(c1,c2,c3)
                        
                
            case '2':
                print (var.getNombre())
            case '3':
                break
            
        
    
c=""
y=""
Biblioteca(c)
    
"""