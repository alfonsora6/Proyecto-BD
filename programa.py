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
    opcion=MostrarMenu()

print("Has salido del programa.")
Desconectar_BD(db)
