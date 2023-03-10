# x=int(input('ingrese valor'))
# print('salidas a consola')
flujo=open('archivos/basico.txt','r')#se crea un objeto de la clase open, esos objetos son rutas que necesitan 3 parametros (la ruta y nombre del archivo .txt,el metodo que va a usar y el tipo de escritura)
#datos=flujo.read()
#print(type(datos))
#flujo.write('Bienvenido al trabajo con archivos')
for dia in flujo:#se itera enn el objeto
    print(dia)
#flujo.close()

with open ('archivos/basico.txt','r') as flujo:
    datos=flujo.read()
    print(datos)

with open ('archivos/basico.txt','r') as flujo:
    for dia in flujo:
        print(dia)