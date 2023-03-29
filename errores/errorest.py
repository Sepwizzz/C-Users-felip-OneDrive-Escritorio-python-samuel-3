def excepcion1():
    try:
        arc = open("archivo.txt")
    except FileNotFoundError:
        print("Ese archivo no esta :c")

#excepcion1()



#excepcion2()

def excepcion3(x):
    try:
        print(x)
    except NameError:
        print("Socio no entiendo que es x")


#excepcion3()