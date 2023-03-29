def oigarfia(pa):
    if (pa[-1]==chr(225) or pa[-1]==chr(233) or pa[-1]==chr(237) or pa[-1]==chr(243) or pa[-1]==chr(250)):
        print("aguda")

    elif (pa[-2]==chr(225) or pa[-2]==chr(233) or pa[-2]==chr(237) or pa[-2]==chr(243) or pa[-2]==chr(250)):
        print("es bla ")
    else:
        print("no es")

    
#oigarfia("león")

#Determinar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula 6
#"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"

# Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula

def Pal():
    Vocales = ["á", "é", "í", "ó", "ú"]
    conso = ["á", "é", "í", "ó", "ú"]
    letrasag = ["n", "s"]
    texto = input("Digite la palabra: ")
    texto.lower()
    for i in Vocales:
        for x in letrasag:
            if i in texto[-1] and x in texto[-1]:
                print("Es aguda")
                break
            if i in texto[-2]:
                print("GRAVE")
                break
            if x in texto[-3]:
                print("es esdrujula")
Pal()

#range(len[texto])