#-Cual es el valor numerico de acuerdo a los códigos del alfabeto
def dord():
    a4="abcdefghijklmnñopqrstuvwxyz"
    listap2=list(a4)
    a=0
    for i in listap2:
        print(i,"tine como numero",ord(i))

dord()

