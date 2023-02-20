#- Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula mate
def cifra():
    cifra={"a":"12","b":"10","c":"9","d":"8","e":"7","f":"6","g":"1","h":"2","i":"3","j":"4","k":"5","l":"16","m":"15","n":"14","ñ":"13","o":"21","p":"20","q":"19","r":"18","s":"17","t":"22","u":"23","v":"24","w":"25","x":"26","y":"88","z":"99"," ":"50"}
    pregunta=input("ponga 1 para poner palabra para cifar\nponga 2 para poner descifar\n")
    #numeros=int(input("ponga numeros del 1 al 28 y = 88 y z = 99 "))
    #letras=input(" es criba palabra para cifrar:")
    if pregunta == "1":
        letras=input("es criba palabra para cifrar:")
        listapla=list(letras)
        listafin2=[]
        for a in listapla:
            a=a
            for i,j in cifra.items():
                if a == i:
                    #print(i)
                    listafin2.append(j)
                    
        print(listafin2)
    elif pregunta== "2":
        numeros2=input("ponga numeros del 1 al 28 y = 88 y z = 99 y pongalos asi 12,23\n")
        
        lista2=[]
        
        listanumeros=numeros2.split(",")
        #print(listanumeros)
        
        for a in listanumeros:
            a=a
            for i,j in cifra.items():
                if a == j:
                    #print(i)
                    lista2.append(i)
        print(lista2)
        #print(listanumeros)
    #hola=2,21,16,12
    #listapla=list(letras)  
    #cifra={"a":12,"b":10,"c":9,"d":8,"e":7,"f":6,"g":1,"h":2,"i":3,"j":4,"k":5,"l":16,"m":15,"n":14,"ñ":13,"o":21,"p":20,"q":19,"r":18,"s":17,"t":22,"u":23,"v":24,"w":25,"x":26,"y":88,"z":99," ":50}
    #for i,j in cifra.items():
    #    if a == j:
    #        print(i)
    #    elif a == i:
    #        print(j)
    
        
cifra()
