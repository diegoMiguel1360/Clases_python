'''Agregación se representa con un rombo blanco en el diagrama de clases
si el objeto o la clase se elimina los objetos agregados NO'''

class Aprendiz:
    def __init__(self,nombre):#constructor clase Aprendiz
        self.__nombre=nombre
        self.__cursos=[]#Se crea una lista vacia

    def agregarCurso(self,titulo):
        self.__cursos.append(titulo)#Se agregan los cursos a la lista vacia

    def getCursos(self):#Metodo getter clase Aprendiz
        return self.__cursos

class Curso:
    def __init__(self,titulo):#Constructor clase Curso
        self.__titulo=titulo

    def getTitulo(self):#Metodo getter clase Curso
        return self.__titulo
    
a=Aprendiz('Martha')
c1=Curso('Python Intermedio')#Los cursos se crean como objetos de la clase Curso y
c2=Curso('Python Basico')#para este momento son independientes de la clase aprendiz
c3=Curso('Introduccion a Java')

a.agregarCurso(c1)#Se agregan los cursos al objeto aprendiz usando el metodo para ello
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos())#Muestra la dirección en memoria de los cursos


for curso in a.getCursos():#se itera la lista cursos creada en la linea 7 usando el metodo getter sobre el objeto
    print(curso.getTitulo())