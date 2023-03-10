def try_syntax(numerator, denominator):#funcion con dos parametros 
    try:
        print(f'In the try block: {numerator}/{denominator}')#imprime los dos parameteos comom los ingreso
        #quiero ver el resultado de la operacion en el print
        result = numerator / denominator#aca hace la operacion 
    except ZeroDivisionError as zde:#especifica el erro y lo asiaga a zde 
        print(zde)#imprime el error 
    else:#si no es cero divicion imprime el resultado 
        print('The result is:', result)
        return result
    finally:# le da final 
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 'a'))