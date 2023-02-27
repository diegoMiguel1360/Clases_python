def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0))

'''Con el comando "as" podemos cambiar el nombre de una o varias entidades, si es mas de una deben estar en parentesis.
en los bloques try-except se pueden usar "else" que funcionan igual que en las condicionales.
el comando finally realiza una acción siempre, no importa el resuldado del bloque try-except, este siempre se ejecutara'''