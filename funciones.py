import sys
import MySQLdb

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db=MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as error:
        print("Error, no se puede conectar a la base de datos",error)
        sys.exit(1)

def Desconectar_BD(db):
    db.close()

def MostrarMenu():
    menu='''
    1- Listar los alumnos y contar cuantas asignaturas tiene cada uno.
    2- Mostrar los alumnos cuya nota media sea superior al valor indicado.
    3- Mostrar nombre de los profesores que dan clases al alumno seleccionado.
    4- Insertar un nuevo alumno.
    5- Eliminar asignatura de la matrícula de un alumno.
    6- Actualizar nota y fecha de una asignatura del alumno indicado.
    7- Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Selecciona una opción: "))
            while opcion<1 or opcion>7:
                print("Error, el número de la opción debe estar comprendido entre el 1 y el 7")
                opcion=int(input("\nSelecciona una opción: "))
            return opcion
        except:
            print("Error, la opción debe de ser un número.\n")

#Ejercicio 1
def Listar_alumnos_y_contar_asignaturas(db):
    sql="SELECT nombre,count(*) as Nº_Asignaturas FROM alumnos,matriculas WHERE id_alumno=alumno GROUP BY nombre"
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        for registro in registros:
            print("Alumno:",registro.get("nombre"),"| Nº de asignaturas:",registro.get("Nº_Asignaturas"))
    except:
        print("Se ha producido un error en la consulta.")

#Ejercicio 2
def agregar_valor_entero():
    try:
        valor=int(input("Introduce un valor: "))
        while valor<1 or valor>=10:
            if valor==10:
                print("La nota media no puede ser mayor que 10.")
                valor=int(input("Introduce un valor: "))
            else:
                print("El valor debe de estar comprendido entre 1 y 10.")
                valor=int(input("Introduce un valor: "))
        return valor    
    except:
        print("El valor indicado debe de ser un número.")
        valor=False
        return valor

def cont_nota_media_superior(db,valor):
    sql="SELECT a.nombre, AVG(m.nota) > %i as media FROM alumnos a,matriculas m WHERE id_alumno=alumno GROUP BY nombre" %valor
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("Alumnos con nota media mayor que %i: "%valor)
        for registro in registros:
            if registro.get("media")>0:
                print("-",registro.get("nombre"))
    except:
        print("Error en la consulta.")

#Ejercicio 3
def listar_alumnos(db):  #Esta función muestra el nombre y apellido de todos los alumnos y además nos lo devolverá en una tupla de diccionarios.
    sql="SELECT nombre,apellido FROM alumnos"
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("\nListado de alumnos:\n")
        for registro in registros:
            print("-",registro.get("nombre"),registro.get("apellido"))
        return registros
    except:
        print("Error en la consulta.")

def mostrar_profesores_de_alumno(db,nombre,apellido): #Esta función nos muestra los profesores de un determinado alumno, y además nos lo devuelve en una tupla de diccionarios.
    sql="SELECT nombre,apellido FROM profesores WHERE id_profesor IN (SELECT profesor FROM asignaturas WHERE id_asignatura IN (SELECT asignatura FROM matriculas WHERE alumno IN(SELECT id_alumno FROM alumnos WHERE nombre='%s' and apellido='%s')))"%(nombre,apellido)
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        #print("Profesores que dan clase a %s %s:"%(nombre,apellido))
        #for registro in registros:
        #    print("-",registro.get("nombre"))
        return registros
    except:
        print("Error en la consulta.")





