from funciones import *

db=Conectar_BD("localhost","alfonso","proyectobd","alumnos")

opcion=MostrarMenu()

while opcion!=7:

    #Ejercicio 1
    if opcion==1:
        print("")
        Listar_alumnos_y_contar_asignaturas(db)
    
    #Ejercicio 2
    elif opcion==2:
        print("")
        valor=agregar_valor_entero()
        print("")
        if valor!=False:
            cont_nota_media_superior(db,valor)

    #Ejercicio 3:
    elif opcion==3:
        alumnos=listar_alumnos(db)
        nombre=input("\nIntroduce el nombre de un alumno: ")
        apellido=input("\nIntroduce el primer apellido de %s: "%nombre)
        profesores=mostrar_profesores_de_alumno(db,nombre,apellido)
        if len(profesores)==0:
            print("\nEl alumno %s %s no tiene profesores."%(nombre,apellido))
        else:
            print("\nProfesores que dan clase a %s %s:\n"%(nombre,apellido))
            for profesor in profesores:
                print("-",profesor.get("nombre"),profesor.get("apellido"))
    
    #Ejercicio 4:
    elif opcion==4:
        id=max_id(db)
        id_nuevo=int(id[0])+1
        alumno={}
        alumno["id_alumno"]=id_nuevo
        alumno["nombre"]=input("Nombre: ")
        alumno["apellido"]=input("Apellido: ")
        #La fecha_nac hay que insertarlo en formato fecha, para mayor claridad, lo he dividido en 3 variables.
        año=input("Introduce el año de nacimiento(YYYY): ")
        mes=input("Introduce el mes de nacimiento(MM): ")
        dia=input("Introduce el día de nacimiento(DD): ")
        alumno["fecha_nac"]="%s-%s-%s"%(año,mes,dia)
        insertar_alumno(db,alumno)
        print("\nLista actual de alumnos:")
        listaalumnos=listar_alumnos(db)

    #Ejercicio 5:
    elif opcion==5:
        mostrar_asignaturas(db)
        asignatura=input("\nSelecciona la asignatura que desee eliminar: ")
        id_asig=id_asignatura(db,asignatura)
        if id_asig != None:
            print("\nLista actual de alumnos:")
            alumnos=listar_alumnos_por_asignatura(db,id_asig[0])
            if alumnos != False:
                if len(alumnos)==0:
                    print("No hay alumnos en la asignatura de %s"%asignatura)
                else:
                    for alum in alumnos:
                        print("-",alum[0])
                    alumno=input("\nSelecciona el alumno: ")
                    id_alum=id_alumno(db,alumno)
                    if id_alum != False:
                        eliminar_asignatura(db,id_alum[0],id_asig[0])
        else:
            print("La asignatura seleccionada no existe.")

    #Ejercicio 6:    
    elif opcion==6:
        matricula={}
        mostrar_asignaturas(db)
        asignatura=input("\nIntroduce el nombre de la asignatura: ")
        id_asig=id_asignatura(db,asignatura)
        matricula["asignatura"]=int(id_asig[0])
        if id_asig != None:
            print("\nLista actual de alumnos:")
            alumnos=listar_alumnos_por_asignatura(db,id_asig[0])
            if alumnos != False:
                if len(alumnos)==0:
                    print("No hay alumnos en la asignatura de %s"%asignatura)
                else:
                    for alum in alumnos:
                        print("-",alum[0])
                    alumno=input("Introduce el nombre del alumno: ")
                    id_alum=id_alumno(db,alumno)
                    if id_alum != False:
                        matricula["alumno"]=int(id_alum[0])
                        nota=float(input("Introduce la nueva nota del alumno: "))
                        while nota<0 or nota>10:
                            print("La nota debe de estar comprendida entre 0 y 10.")
                            nota=float(input("Introduce la nueva nota del alumno: "))
                        matricula["nota"]=nota
                        año=input("Introduce el año de la nueva fecha(YYYY): ")
                        mes=input("Introduce el mes de la nueva fecha(MM): ")
                        dia=input("Introduce el día de la nueva fecha(DD): ")
                        matricula["fecha"]="%s-%s-%s"%(año,mes,dia)
                        actualizar_notayfecha_de_asignatura(db,matricula)
    opcion=MostrarMenu()

print("Has salido del programa.")
Desconectar_BD(db)
