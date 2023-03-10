from carga import * #se importa la clase carga
from conductor import * #se importa la clase conductor
# c1=Conductor('Luis',12345)   intancia objeto de la clase conductor
# carga1=Carga('aaa-123',c1,5,2)   instancia objeto de la clase carga
# print(carga1)
nomConductor=input('Ingrese nombre del conductor') #se declara variable con el nombre del conductor introducido por teclado
docConductor=int(input('Ingrese documento del conductor')) #se declara variable de tipo entero documento de conductor introducido por el teclado
placa=input('ingrese placa') #se declara variable con la placa del vehiculo introducido por teclado
capacidad=input('ingrese capacidad en toneladas') #se declara variable con la capacidad introducido por teclado
ejes=input('ingrese numero de ejes') #
c1=Conductor(nomConductor,docConductor) #se instancia el objeto c1 de la clase conductor y se asocian la variables correspondientes como parametros
obCarga=Carga(placa,c1,capacidad,ejes) #se instancia el objeto obcarga de la clase carga y se asocian la variables correspondientes como parametros
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento()) #variable con los atributos del conductor asociado al objeto carga

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes()) #variable con todos los atributos de la carga

with open('poo-archivos/listado.txt','a') as flujo: #creo "w" o agrego "a" al archivo listado.txt por medio del objeto flujo
    flujo.write(cadCarga+'\n') #uso el metodo write en el objeto flujo para escribir los atributos de la carga, no olvidar \n para salto de linea