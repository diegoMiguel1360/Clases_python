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
    def __init__(self,id,nombres,apellidos,edad,telefono,email,contraseña,profesion,certificado):
        super().__init__(id,nombres,apellidos,edad,telefono,email,contraseña)
        self.profesion=profesion
        self.__certificado=certificado
        self.__materias_asignadas=[]

    def getInstructor(self):
        return self.getUsuario(),self.profesion,self.__certificado
    def getMaterias_asignadas(self):
        return self.__materias_asignadas
    
    def setProfesion(self,profesion):
        self.profesion=profesion
    def setCertificado(self,certificado):
        self.__certificado=certificado

    def agregar_materia(self,materia):
        self.__materias_asignadas.append(materia)
        
    def procesar_matricula(self,matricula):
        return

class Estudiante(Usuario):
    def __init__(self,id,nombres,apellidos,edad,telefono,email,contraseña):
        super().__init__(id,nombres,apellidos,edad,telefono,email,contraseña)
        self.curso=''
        self.jornada=''
        self.semestre=0
    
    def getEstudiante(self):
        return self.getUsuario(),self.curso,self.jornada,self.semestre
        
    def generar_inscripcion(self,nueva_inscripcion,detalle,requisitos,fecha,id_curso,jornada):
        self.__nueva_inscripcion=Inscripcion(nueva_inscripcion,detalle,requisitos,fecha,id_curso,jornada)
        self.curso=id_curso
        self.jornada=jornada
        self.semestre+=1

class Matricula:
    def __init__(self,id,detalle,fecha,valor):
        self.__id=id
        self.detalle=detalle
        self.fecha=fecha
        self.__valor=valor

class Materia:
    def __init__(self,id,nombre,descripcion):
        self.__id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.cronograma=''
        self.__instructor=''

class Inscripcion:
    def __init__(self,id,detalle,requisitos,fecha,id_curso,jornada):
        self.__id=id
        self.detalle=detalle
        self.requisitos=requisitos
        self.fecha=fecha
        self.__id_curso=id_curso
        self.jornada=jornada
        self.__estado='pendiente'

class Curso:
    def __init__(self,id,nombre,descripcion,fecha,nivel,cupo):
        self.__id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha=fecha
        self.nivel=nivel
        self.cupo=cupo
        self.__pensum=[]
        self.__integrantes=[]
        
    def getCurso(self):
        return self.__id,self.nombre,self.descripcion,self.fecha,self.nivel
    

    
    

us=Usuario(1546,'diego','moreno',12,156456,'ssff','dgdg')
#us.generar_inscripcion(123,'dfdsf','sdds',32323,654,'M')
print(us.getUsuario())
as1=Usuario(548654,'miguel','sanchez',5646,87564,'dhfgdj','dhfdjk')

