import sqlite3 #importa modulo sqlite

with sqlite3.connect('sqlitepython/conpython.db')as con:#con el metodo with creamos un flujo al archivo db
    micursor=con.cursor()#instanciamos un objeto cursor usando el flujo creado
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"#la sentencia es el codigo SQL
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):#definimos la funcion miselect con 5 parametros
    micursor=conexion.cursor()#instanciamos un objeto cursor usando el flujo creado en la linea 3
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"#usamos la plantilla literal para definir la sentencia usando los parametros de la funcion
    #print(sentencia)
    print(micursor.execute(sentencia).fetchall())#se ejecuta la sentencia con el metodo .execute() y traemos todos los campos con .fetchall()

def modificar(con,tabla,campo,dato,id):
    micursor=con.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato} WHERE id = '{id}';"
    micursor.execute(sentencia)
    con.commit()#Este metodo se usa cuando se requiera modificar información en db
    print("Modificacion correcta")

def eliminar(con,tabla,campo,dato):
    micursor=con.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()#
    print("Eliminacion correcta")



miselect(con,'alumno','email','=','dbrabon2@irs.gov')#se llama la funcion con los parametros necesarios
modificar(con,'alumno','nombre','Vegeta',1)
eliminar(con,'alumno','id',3)