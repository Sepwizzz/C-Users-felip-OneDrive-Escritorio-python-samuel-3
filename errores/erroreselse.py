def numerop6():
    try:
        lista=[1,2,3,4]
        a=int(input("hola:"))
        #assert a == lista,"este numero esta prohibido"
        print("su numero edad:",a)
        assert a > 17
    except AssertionError:
        print("profavor ponga un adulto")
    except ValueError:
        print("ponga un numero numerico")
        numerop6()
    else:
        return
    
#numerop6()

def numerosproi1():
    try: 
        a=int(input("ponga: "))
        ae =[2001,9,11,777,666]
        if a in ae:
            print(a, "esta prohibido en mi sistema")
        elif a not in ae:
            print("usted dijito",a)
    except ValueError:
        print("no admito  ese valor")
        numerosproi1()

    except UnboundLocalError:
        print("me perdi")
    else:
        print("gracias")


numerosproi1()
