numero1=0

def notas():
    numero1=0
    numero1 = int(input("ingrese nota:"  ))
    if  numero1 <= 4:
        print("insufisiente")
    elif  numero1 <= 6:
        print ("suficiente")
    elif  numero1 <= 10:
        print("bien")
    return " "
print(notas (  ))
