#- De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

def contadordecv():
  
    palabra=input("ponga palabra:")

    caracter="!#$%‰&()*+,-./-:;<<=>>?@-[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼¿ÂÃÄÅÆÇÌÍÎÏÐÑÒÔÕÖ×ØÙÚÛÜÝÞßâãäåæçêëîïðñôõö÷øûüýþÿ€≠≤≥√Ω↑↓←→↔№▲►▼◄■□▪▫●○◊"
    vocales="aeiouAEIOU"
    consonante="CDFGHJKLMNÑPQRSTVXZWYcdfghjklmnñpqrstvxzwy."
    vocalestil="áéíóúÁÉÍÓÚ"
    
    listap=list(palabra)
    listavocales=list(vocales)
    listaca=list(caracter)
    litaconso=list(consonante)
    listavocaltil=list(vocalestil)
    
    #print(listaca)
    #print(listavocales)
    #print(listap)
    conutca=0
    countvocale=0
    vocaltil=0
    conso=0
    
    listafin=[]
    for r in listap:
        listafin.append(r)
        for i in listaca:
            if r == i:
                conutca=conutca+1
        for a in listavocales:
            if r == a:
                countvocale=countvocale+1
        for t in listavocaltil:
            if r == t:
                vocaltil=vocaltil+1
        for f in litaconso:
             if r == f:
                conso=conso+1
    
        
        
    print(palabra,"\ntiene estos numeros de caracters:",conutca,"\ntiene este numero de volacles:",countvocale,"\ntine este numero de vovales con tilde:",vocaltil,"\ntine este numero de consonantes:",conso)    
                    
    
            
contadordecv()
    
    

    