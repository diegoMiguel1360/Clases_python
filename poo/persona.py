class Persona: #El comando reservado class para iniciar la clase, nombre de la clase y 2 puntos donde empieza el bloque de codigo
    def __init__(self,nombre,documento,telefono):#metodo constructor inicia la creacion de objeto, siempre lleva el parametro self que se refiere a la misma clase
        self.__nombre=nombre#atributo del objeto, __ al inicio del atributo lo convierte en privado
        self.__documento=documento
        self.telefono=telefono
        print('Activando constructor')

    def getUsuario(self):#metodo getter para obtener los datos del objeto
        return self.__documento,self.__nombre,self.telefono
    
    def setNombre(self, nombre):#metodo setter para modificar los datos del objeto
        self.__nombre=nombre

    def setDocumento(self,documento):
        self.__documento=documento

    def setTelefono(self,telefono):
        self.telefono=telefono

    def metodo(self):
        print('Soy un método')


ob=Persona('Ana',52458423,3201546877)#instanciacion del objeto ob cuyo nombre es Ana
print(ob.getUsuario())#llamamos el metodo get que contiene el atributo nombre
ob.setNombre('Maria')#usamos el metodo set para cambiar el nombre del objeto
ob.setDocumento(10215578)
ob.setTelefono(3145789)
print(ob.getUsuario())
#ob.metodo()
#print(type(ob))