class Conductor:#se crea la clase conductor
    def __init__(self,nombre,documento):#constructor
        self.__nombre=nombre#declara variables
        self.__documento=documento
    def getNombre(self):#metodo getter
        return self.__nombre
    def getDocumento(self):
        return self.__documento