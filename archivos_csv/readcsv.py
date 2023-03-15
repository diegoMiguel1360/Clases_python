from Aprendiz import *
import csv
listaAprendices=[]
#with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
with open('archivos_csv\\enterprices.csv') as csvDataFile:
#with open('https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html/addresses') as csvDataFile:
    csvReader=csv.reader(csvDataFile)

    for rows in csvReader:
        #apr=Aprendiz(row[2],row[3],row[4],row[5])
        #listaAprendices.append(apr)
        print(row)
        #print('first name:',row[0])
        #print('last name:',row[1])
        #print('email:',row[2])
        #print('id:',row[3])
print(listaAprendices)
for apr in listaAprendices:
    print(apr.nombreCompleto())