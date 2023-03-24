from permios import*
import csv
listaoscar=[]
with open("D:\\a2\\samuel t3\\archivos\\oscarm.csv") as csvDataFile:

    csvReader=csv.reader(csvDataFile)    
    for row in csvReader:
        
        ob=premioso(row[0],row[1],row[2],row[3],row[4])
        listaoscar.append(ob)
        
        # print('first name:',row[0])
        # print('last name:',row[1])
        # print('email:',row[2])
        # print('id:',row[3])
"""print(listaoscar)
for aprendiz in listaoscar:
    print(aprendiz.getpeliculasn())
print(listaoscar[10])"""

with open("D:\\a2\\samuel t3\\archivos\\osacarf.csv") as csvf:
    csvfame=csv.reader(csvf)    
    for m in csvfame:
            
            ob=premioso(m[0],m[1],m[2],m[3],m[4])
            listaoscar.append(ob)
            
            # print('first name:',row[0])
            # print('last name:',row[1])
            # print('email:',row[2])
            # print('id:',row[3]) 


for osc in listaoscar:
     pass
    #print(osc.getpeliculasn())
 

#pelicula=input("que pelicula desea buscar:")
pelicula="Name"

if pelicula in listaoscar[0]:

    print("si esta ")
else:
    print("no")





