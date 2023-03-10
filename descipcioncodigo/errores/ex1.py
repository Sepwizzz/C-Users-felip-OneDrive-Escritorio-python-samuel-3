""""
try:
    #print(1/1))
    raise SyntaxError #con el raise le dice a pytho que lance el error llamdo SyntaxError sea como sea 
except SyntaxError as e: # aca toma SyntaxError y lo asigna auna variable o le cambia el nombre 
    print(e)#imprime e que e es SyntaxError
    print('Cierra el parentesis')
"""
try:
    #raise ZeroDivisionError
    print(1/0)
    #raise ZeroDivisionError
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:
    print(zde)
    #print('prueba error')