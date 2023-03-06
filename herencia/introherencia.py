class A1:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A1')

class A2:
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde A2')


class B(A2,A1):#La clase B es hija de las clases A2 y A1
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):
        return 'Soy un objeto de la clase B'
obj=B()#Al instacnciar un objeto de la clase B, este hereda los metodos de las clases padre (A2,A1)
print(obj.__str__())
obj.saludo()#Si Python no encuentra el metodo invocado en la subclase, este buscará en las clases padre según el orden de izquierda a derecha
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())
