values = (1, 0)#values tiene asignado sos numeros  que 1,0
#x,y=10,12
#print(divmod(10,3))
try:
    q, r = divmod(*values)# q vale 1 y r vale 0  es una funcion integrada 
    #print('valor de q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)