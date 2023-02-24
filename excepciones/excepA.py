try:
    #print(1/1))
    raise SyntaxError
except SyntaxError:
    print('Cierra el parentesis')

'''La excepción de sintaxis no se maneja con try como las demas ya que es innecesario corregir un error que el mismo programador cometio a proposito, 
pero para poder usarla en este caso podemos utilizar el comando raise y asi generarla artificialmente'''