print("cuestionario")

print("este cuestionario tiene como unica respuesta 'v' (verdadero) 'f' (falso)")
print("el programa solo reconoceralas respuestas en MAYUSCULAS")

pregunta1 = "¿fue colon la persona que descurbrio America?"
pregunta2= "¿la independencia de colombia fue en el año 1810?"
pregunta3 = "¿ the doors era un grupo de rock Americano?"

respuesta1 = "V"
respuesta2 = "V"
respuesta3 = "V"

formulacion1 =input(f"pregunta 1 : {pregunta1}")
formulacion2 =input(f"pregunta 2 : {pregunta2}")
formulacion3 =input(f"pregunta 3 : {pregunta3}")

corecto1 = False
corecto2 = False
corecto3 = False

#pregunta 1
if (formulacion1 == respuesta1):
    corecto1 = True
else:
    corecto1 = False
    
#pregunta 2
if (formulacion2 == respuesta1):
    corecto2 = True
    
else:
    corecto2 = False
    
#pregunta 3
if (formulacion3 == respuesta1):
    corecto3 = True
    
else:
    corecto3 = False
    
#respuesta 1
if (corecto1 == True):
    print("pregunta 1 es correcta")
    
else:
    print("pregunta 1 es incorrecta")    
    
#respuesta 2
if (corecto2 == True):
    print("pregunta 2 es correcta")

else:
    print("pregunta 2 es incorrecta")
    
#respuesta 3
if (corecto3 == True):
    print("pregunta 3 es correcta")
    
else:
    print("pregunta 3 es incorrecta")
    