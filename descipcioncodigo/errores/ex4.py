def edad():#funcion sin parametro 
    try:
        tuedad=int(input("introduce tu edad"))# pide que dijite una edad de un valor entero 
        print(f'tu edad es  {tuedad}')#imprime la edad 
        #print('Tu edad es ',tuedad)
    except ValueError as e:    # espesifica el error de vauleerror
        print(e)#imprime el errro 
        print("La edad debe ser un valor numerico...")# un messaje
        edad()# y llama la funcion edad para que se repita hata que ponga una edad verdadera 
    
edad()