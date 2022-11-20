import random

list =random.randint(10,26)
A=[]
cuenta = 0
acomu = cuenta
for i in range (list):
    A.append(round(random.random()*25))
print(A)
N = 0
e = A
print(A[N])
N=int(input("ingrese el numero: "))
print(A[N])