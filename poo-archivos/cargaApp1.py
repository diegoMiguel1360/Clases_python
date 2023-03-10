with open('poo-archivos/listado.txt','r') as flujo: #leo "r" el archivo listado.txt por medio del objeto flujo
    ob=flujo.read() #uso el metodo write en el objeto flujo para escribir los atributos de la carga, no olvidar \n para salto de linea

carg1=ob.split('\n')
print(carg1)

for i in range (len(carg1)-1):
    carg2=carg1[i].split(',')
    print(carg2)
    for j in carg2:
        print(j)
