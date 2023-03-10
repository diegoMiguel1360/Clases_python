from vehiculo import * #se importa la clase vehiculo
class Carga(Vehiculo):#se crea la clase carga que es subclase de vehiculo, por eso se importa
    def __init__(self,placa,conductor,capacidad,ejes):#constructor clase carga
        Vehiculo.__init__(self,placa,conductor)#constructor superclase vehiculo
        self.__capacidad=capacidad#se declara variable self.__capacidad
        self.__ejes=ejes    #se declara variavle self.__ejes
    def getCapacidad(self):#metodo getter
        return self.__capacidad    
    def getEjes(self):#metodo getter
        return self.__ejes