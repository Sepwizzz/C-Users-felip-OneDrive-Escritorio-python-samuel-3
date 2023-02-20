#- cuantas veces se repite un caracter dado
def palacount():
    pala=input("ponga palabra:")
    lista1=list(pala)
    lista2=list(pala)
    s=0
    for i in lista1:
        i=i
        for j in lista2:
            j=j
        if i==j:
            s=s+1
    print(s)

palacount()