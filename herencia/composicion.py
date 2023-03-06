'''Composicion se representa con un rombo negro en el diagrama de clases
si el objeto o la clase se elimina los objetos creados tambien'''

class Curso:
    def __init__(self,titulo):#Constructor
        self.__titulo=titulo#Se crea la variable con el titulo del curso

    def getTitulo(self):#Metodo get para ver el titulo del objeto
        return self.__titulo

class Aprendiz:
    def __init__(self,nombre):#Constructor
        self.__nombre=nombre
        self.__cursos=[]#Se crea una lista vacia

    def agregarCurso(self,nombreCursito):
        cursito=Curso(nombreCursito)#se crea el objeto cursito de la clase Curso
        self.__cursos.append(cursito)# se agregan los objetos Curso a la lista

    def getCursos(self):#Metodo get para ver el nombre del curso
        return self.__cursos
    
ap=Aprendiz('Sofia')#instanciamos el objeto ap de la clase Aprendiz
ap.agregarCurso('Python Basico')#llamamos el metodo agregarCurso
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():#Se itera la lista cursos creada en la liena 14
    print(c.getTitulo())#se muestran los cursos
