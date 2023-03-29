def numerosproi1():
    try: 
        a=int(input("ponga: "))
        ae =[2001,9,11,777,666]
        if a in ae:
            print(a, "esta prohibido en mi sistema")
        elif a not in ae:
            print("usted dijito",a)
    except ValueError:
    #except UnboundLocalError:
        print("no admito  ese valor")
    #except ValueError:
    except UnboundLocalError:
        print("me perdi")

#numerosproi1()

def sancocho2():
    try:
        a=int(input('sancocho :'))
        lstSancocho=['agua','papa','yuca','pollo','arracacha','platano','silantro','aji(opcional)','pola para compañia','y si tiene plata echele mas']
        print(lstSancocho[a])
    except IndexError:
        print("no hay olla pal sancocho")
    except ValueError:
        print('sancocho sin papá')

#sancocho2()


def edad ():
    
    a=int(input("ponga numero"))
    
    assert a>0," usted no anacido"
    print("aq")

#edad3()

def excepcion4():
    try:
        arc = open("archivo.txt")
    except FileNotFoundError:
        print("Ese archivo no esta :c")

#excepcion4()

def excepcion5(x):
    try:
        print(x)
    except NameError:
        print("Socio no entiendo que es x")


#excepcion5()
#NameError,FileNotFoundError,IndexError,UnboundLocalError