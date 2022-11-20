import random
list =random.randint(10,25)
A=[]
n = len(A)
cuenta = 0
acomu = cuenta
for i in range (list):
    A.append(round(random.random()*25))
for i in range(n):
    cuenta = 0
    for j in range(n):
        if (A[i] == A[j] ):
            i=i+cuenta
            cuenta= i

print("lista= ",A[i],"se repite",acomu,"veces")
print(A)