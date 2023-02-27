values = (1, 0)
#x,y=19,30
#print(divmod(10,3))
try:
    q, r = divmod(*values)
    #print('q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)

'''divmod() toma 2 valora numericos y devuelve el cociente y el residuo del primero entre el segundo.
si usamos un * antes de una tupla o lista podemos descomponerla en sus valores contenidos.
La forma f'{}' sirve para imprimir cadenas junto con variables usando menos codigo
'''