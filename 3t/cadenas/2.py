#- Pida una cadena por teclado y diga cual es su valor al sumar sus codigos

def pala():
    palabra=input("ponga palabra:")
    listap2=list(palabra)
    a=0
    for i in listap2:
        a+=ord(i)
    print(a)

pala()
#print(ord(a))
#print(ord(i))