class Vehiculo:#se crea la clase vehiculo
    def __init__(self,placa,conductor):#constructor
        self.__placa=placa#declara variables
        self.__conductor=conductor
    def getConductor(self):#metodo getter
        return self.__conductor
    def getPlaca(self):
        return self.__placa