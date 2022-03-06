from funciones import *

db=Conectar_BD("localhost","usuario","asdasd","testdb")

opcion=MostrarMenu()

while opcion!=7:
    if opcion==1:
        print("")
        Listar_alumnos_y_contar_asignaturas(db)

    opcion=MostrarMenu()

print("Has salido del programa.")
Desconectar_BD(db)
