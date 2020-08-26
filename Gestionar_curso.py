import os
import sys
import time

def Gest():
    while True:
        os.system('cls')
        print("------Gestionar cursos-------")
        print("\t1 - Listar Cursos")
        print("\t2 - Mostrar Cursos")
        print("\t3 - Agregar Curso")
        print("\t4 - Editar Curso")
        print("\t5 - Eliminar Curso")
        print("\t6 - Regresar")
        print("-----------------------------")
        menuGestionar = input("Eliga una de las 6 opciones: ")
        if menuGestionar == "1":
            print("hola")
        elif menuGestionar == "2":
            print("hola")
        elif menuGestionar == "3":
            print ("hola")
        elif menuGestionar =="4":
            print("hola")
        elif menuGestionar =="5":
            print("hola")
        elif menuGestionar =="6":
            time.sleep(2)
            break
        else:
            print("Seleccione una opcion valida")
            time.sleep(1)
#Gest()