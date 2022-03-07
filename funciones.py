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
    sql="select nombre,count(asignatura) as Nº_Asignaturas from alumnos a left join matriculas m on a.id_alumno=m.alumno group by nombre"
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
        return registros
    except:
        print("Error en la consulta.")

#Ejercicio 4:
def max_id(db):
    sql="SELECT MAX(id_alumno) from alumnos"
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        registro=cursor.fetchone()
        return registro
    except:
        print("Se ha producido un error al calcular el mayor identificador.")

def insertar_alumno(db,alumno):
    cursor=db.cursor()
    sql="INSERT INTO alumnos values ('%i','%s','%s','%s')" %(alumno.get("id_alumno"),alumno.get("nombre"),alumno.get("apellido"),alumno.get("fecha_nac"))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("\nError al insertar los datos.")
        db.rollback()

def listar_alumnos(db):
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    sql="SELECT nombre from alumnos"
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        for registro in registros:
            print("-",registro.get("nombre"))
        return registros
    except:
        print("Se ha producido un error en la consulta.") 

#Ejercicio 5:
def mostrar_asignaturas(db):
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    sql="SELECT * FROM asignaturas"
    try:
        cursor.execute(sql)
        asignaturas=cursor.fetchall()
        print("\nLista de asignaturas:\n")
        for asignatura in asignaturas:
            print("-",asignatura.get("nombre"))
    except:
        print("Se ha producido un error en la consulta.")

def id_asignatura(db,asignatura):
    sql="SELECT id_asignatura FROM asignaturas WHERE nombre='%s'"%asignatura
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        registro=cursor.fetchone()
        return registro
    except:
        print("Se ha producido un error al calcular el identificador de la asignatura.")

def listar_alumnos_por_asignatura(db,asignatura):
    sql="SELECT nombre FROM alumnos WHERE id_alumno IN (SELECT alumno FROM matriculas WHERE asignatura=%i)"%asignatura
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        return registros
    except:
        print("Error, no hay alumnos pertenecientes a esa asignatura.")
        error=False
        return error

def id_alumno(db,alumno):
    sql="SELECT id_alumno FROM alumnos WHERE nombre='%s'"%alumno
    cursor=db.cursor()
    try:
        cursor.execute(sql)
        if cursor.rowcount!=0:
            registro=cursor.fetchone()
            return registro
        else:
            print("El alumno no existe.")
            return False
    except:
        print("Se ha producido un error al calcular el identificador del alumno.")

def eliminar_asignatura(db,alumno,asignatura):
    sql="DELETE FROM matriculas WHERE alumno=%i and asignatura=%i"%(alumno,asignatura)
    cursor=db.cursor()
    respuesta=input("¿Desea continuar? s/n: ")
    if respuesta=="s":
        try:
            cursor.execute(sql)
            db.commit()
            print("La asignatura se ha eliminado correctamente.")
        except:
            print("Error al eliminar la asignatura.")
            db.rollback()

#Ejercicio 6: 

def validar_nota():
    try:
        nota=float(input("Introduce la nueva nota del alumno: "))
        return nota
    except:
        print("Error, la nota debe de ser decimal.")
        return False


def actualizar_notayfecha_de_asignatura(db,matricula):
    cursor=db.cursor()
    sql="UPDATE matriculas SET fecha=%s WHERE alumno=%i and asignatura=%i"%(matricula.get("año"),matricula.get("alumno"),matricula.get("asignatura"))
    sql2="UPDATE matriculas SET nota=%.2f WHERE alumno=%i and asignatura=%i"%(matricula.get("nota"),matricula.get("alumno"),matricula.get("asignatura"))
    try:
            cursor.execute(sql)
            cursor.execute(sql2)
            db.commit()
            print("La fecha y nota se han actualizado correctamente.")
    except:
        print("Error al actualizar la nota y fecha.")
        db.rollback()
