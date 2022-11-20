import random
list =random.randint(10,20)
list =[random]
num = 1
def es_primo_2(inicial,final):
    
    primos =[]
    for n in range(9,25+1):
        es_primo = True
        for i in range(9,26):
            if n % i == 0:
                 es_primo = False
            break
        
   
print (list)
print("esprimo", es_primo_2 )