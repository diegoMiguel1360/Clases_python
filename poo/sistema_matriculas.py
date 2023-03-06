class Usuario:
    def __init__(self,id,nombres,apellidos,edad,telefono,email,contraseña):
        self.__id=id
        self.__nombres=nombres
        self.__apellidos=apellidos
        self.edad=edad
        self.telefono=telefono
        self.email=email
        self.__contraseña=contraseña
    
    def getUsuario(self):
        return self.__id,self.__nombres,self.__apellidos,self.edad,self.telefono,self.email
    
    def setEdad(self,edad):
        self.edad=edad
    def setTelefono(self,telefono):
        self.telefono=telefono
    def setEmail(self,email):
        self.email=email

class Instructor(Usuario):
    def __init__(self, id, nombres, apellidos, edad, telefono, email, contraseña,profesion,certificado):
        super().__init__(id, nombres, apellidos, edad, telefono, email, contraseña)
        self.profesion=profesion
        self.__certificado=certificado
        self.__cursos_asignados=[]

    def getCertificado(self):
        return self.profesion,self.__certificado
    def getCursos_asignados(self):
        return self.__cursos_asignados
    
    def setProfesion(self,profesion):
        self.profesion=profesion
    def setCertificado(self,certificado):
        self.__certificado=certificado

    def agregar_curso(self,curso):
        self.__cursos_asignados.append(curso)

class Estudiante(Usuario):
    pass

us=Usuario(1546,'diego','moreno',12,156456,'ssff','dgdg')
print(us.getUsuario())
