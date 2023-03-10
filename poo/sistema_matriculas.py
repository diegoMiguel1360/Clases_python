class Acta:
    def __init__(self,id,detalle,fecha,valor):
        self.__id=id
        self.detalle=detalle
        self.fecha=fecha
        self.__valor=valor

    def getActa(self):
        return self.__id,self.detalle,self.fecha,self.__valor
    
    def setDetalle(self,detalle):
        self.detalle=detalle
    def setFecha(self,fecha):
        self.fecha=fecha
    def setValor(self,valor):
        self.__valor=valor
        
    def genera_cobro(self):
        print('Debe pagar $ 50.000')

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
    
    def setNombres(self,nombres):
        self.__nombres=nombres
    def setApellidos(self,apellidos):
        self.__apellidos=apellidos
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

    def getInstructor(self):
        return self.getUsuario() + (self.profesion,self.__certificado)
    
    def setProfesion(self,profesion):
        self.profesion=profesion
    def setCertificado(self,certificado):
        self.__certificado=certificado
        
    def procesar_acta(self,acta):
        if isinstance(acta,Acta):
            print(f'acta nro {acta} procesada')
        else:
            print('Digite un acta')
            #self.procesar_acta(acta)

class Estudiante(Usuario):
    def __init__(self,id,nombres,apellidos,edad,telefono,email,contraseña):
        super().__init__(id,nombres,apellidos,edad,telefono,email,contraseña)
        self.curso=''
        self.jornada=''
        self.semestre=0
    
    def getEstudiante(self):
        if self.curso=='':
            return self.getUsuario()
        else:
            return self.getUsuario()+(self.curso,self.jornada,self.semestre)
        
    def generar_acta(self,id, detalle, fecha, valor,acta):
        self.acta=acta
        self.acta=Acta(id, detalle, fecha, valor)
        print(self.acta.getActa())
        self.acta.genera_cobro()

class Materia:
    def __init__(self,id,nombre,descripcion):
        self.__id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.cronograma=''
        self.__instructor=[]
    
    def getMateria(self):
        return self.__id,self.nombre,self.descripcion
    def getCronograma(self):
        return self.cronograma
    def getInstructor(self):
        return self.__instructor
    
    def setNombre(self,nombre):
        self.nombre=nombre
    def setCronograma(self,cronograma):
        self.cronograma=cronograma
    
    def agregarInstructor(self,instructor):
        self.__instructor.append(instructor)

class Inscripcion:
    def __init__(self,id,detalle,requisitos,fecha):
        self.__id=id
        self.detalle=detalle
        self.requisitos=requisitos
        self.fecha=fecha
        self.__estudiantes=[]

    def getInscripcion(self):
        return self.__id,self.detalle,self.requisitos,self.fecha
    
    def setDetalle(self,detalle):
        self.detalle=detalle
    def setRequisitos(self,requisitos):
        self.requisitos=requisitos
    def setFecha(self,fecha):
        self.fecha=fecha
    
    def agregar_alumno(self,alumno):
        if self.__estudiantes==None:
            self.__estudiantes.append(alumno)
        else:
            print('Ya existe un alumno relacionado a esta inscripcion')

class Curso:
    def __init__(self,id,nombre,descripcion,fecha,nivel,cupo):
        self.__id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha=fecha
        self.nivel=nivel
        self.cupo=cupo
        self.__pensum=[]
                
    def getCurso(self):
        return self.__id,self.nombre,self.descripcion,self.fecha,self.nivel
    def getPensum(self):
        return self.__pensum
    def getAlumnos(self):
        return self.__alumnos
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    def setFecha(self,fecha):
        self.fecha = fecha
    def setCupo(self,cupo):
        self.cupo = cupo
        
    def agregarMateria(self,materia):
        self.__pensum.append(materia)
    
    def inscribir(self,id,detalle,requisitos,fecha):
        self.__alumnos=Inscripcion(id, detalle, requisitos, fecha)
        

#-----------------------------------------------
    
a=0
while a==0:
    print('\n***MENU***')
    print('1. Estudiantes')
    print('2. Instructores')
    print('3. Cursos')
    print('4. Materias')
    print('5. Inscribiciones')
    print('0. Salir')
    opcion=int(input('Digite una opcion: '))
    if opcion==1:
        a1=0
        lista1=[]
        while a1==0:
            print('\n***ESTUDIANTES***')
            print('1. Registrar estudiante')
            print('2. Mostrar estudiantes')
            print('3. Buscar estudiante')
            print('4. Modificar estudiante')
            print('0. Salir')
            opcion1=int(input('Digite una opcion: '))
            if opcion1==1:
                print('\n***REGISTRAR ESTUDIANTE***')
                eid=input('id: ')
                enom=input('nombres: ')
                eape=input('apellidos: ')
                eeda=input('edad: ')
                etel=input('telefono: ')
                eema=input('email: ')
                econ=input('contraseña: ')
                est=Estudiante(eid, enom, eape, eeda, etel, eema, econ)
                lista1.append(est)
                print('--ESTUDIANTE REGISTRADO CON EXITO--')
            elif opcion1==2:
                print('\n***MOSTRAR ESTUDIANTES***')
                for i in lista1:
                    print(i.getEstudiante())
            elif opcion1==3:
                print('***BUSCAR ESTUDIANTE***')
                x=input('Digite id del usuario: ')
                for i in lista1:
                    tup=i.getEstudiante()[:1]
                    for j in tup:
                        if x==j:
                            print(i.getEstudiante())
                        else:
                            print('Estudiante no existe')
            elif opcion1==4:
                print('***MODIFICAR ESTUDIANTE***')
            elif opcion1==0:
                break
            else:
                print('opcion invalida')
    elif opcion==2:
        print('***INSTRUCTORES***')
    elif opcion==3:
        print('***CURSOS***')
    elif opcion==4:
        print('***MATERIAS***')
    elif opcion==5:
        print('***INSCRIPCIONES***')
    elif opcion==0:
        exit()
    else: print('opcion invalida')
        