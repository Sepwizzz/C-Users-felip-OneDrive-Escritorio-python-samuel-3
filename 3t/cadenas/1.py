#a=["hola","como","estas","?"]
#print("------".join(["hola","como","estas","?"]))
#A2="Hola Mi Pana"
#print(A2.lower())
#a3="  hola"
#print(a3.lstrip())
#a4="abcdefghijklmnñopqrstuvwxyz"
#print(len(a4))
#A12= list(a4)
#print(len(A12))
#print(A12)
#- Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
def ar():
    s=0
    pala=input("ponga palabra:")
    listap= list(pala)
    s=0
    conta=0
    list=[]
    #print(listap)
    for i in pala:
        i=i
        if i not in list :
            list.append(i)
            conta+=1
    print(conta)
        
        

