
num1 = int(input("dijite un numero:  "))
num2 = int(input("dijite un numero:  "))
num3 = int(input("dijite un numero:  "))

def igual(num1,num2,num3):
    if num1==num2==num3:
        print("los tres son iguales")
    elif num1==num2:
        print(" primero y segundo son iguales ")
    elif num1==num3:
        print("primero y tercero son iguales")
    elif num2==num3:
        print("segundo y tercero son iguales")
    else:
        print("nigunnumero es igual")
    

    
print (igual(num1,num2,num3))