from funciones import *

db=Conectar_BD("localhost","usuario","asdasd","testdb")

opcion=MostrarMenu()

while opcion!=7:

    #Ejercicio 1
    if opcion==1:
        print("")
        Listar_alumnos_y_contar_asignaturas(db)
    
    #Ejercicio 2
    elif opcion==2:
        valor=agregar_valor_entero()
        print("")
        if valor!=False:
            cont_nota_media_superior(db,valor)

    opcion=MostrarMenu()

print("Has salido del programa.")
Desconectar_BD(db)
