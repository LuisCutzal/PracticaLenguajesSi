import os
import sys
import time
import Funciones

def Listar():
    print("Eligio Listar Cursos")
    print("espere...")
    time.sleep(2)
    Funciones.Listar()

def Agregar():
    print("Eligio Agregar Curso")
    print("espere...")
    time.sleep(2)
    Funciones.Agregar()

def Mostrar():
    print("Eligo Mostrar Curso")
    print("espere...")
    time.sleep(2)
    Funciones.Mostrar()

def Editar():
    print("Eligio Editar Curso")
    print("espere...")
    time.sleep(2)
    Funciones.Modificar()

def Eliminar():
    print("Eligio Eliminar Curso")
    print("espere...")
    time.sleep(2)
    Funciones.Eliminar()


def CreditosAprobados():
    #print("Eligio Creditos Aprobados")
    print("espere...")
    time.sleep(2)
    Funciones.CreditosAprobados()

def CreditosCursando():
    #print("Eligo Credritos Cursando")
    print("espere...")
    time.sleep(2)
    Funciones.CreditosCursando()

def CreditosPendientes():
    #print("Eligio Creditos Pendientes")
    print("espere...")
    time.sleep(2)
    Funciones.CreditosPendientes()

def CreditosObligatorios():
    #print("Eligio Creditos Obligatorios")
    print("espere...")
    time.sleep(2)
    Funciones.CreditosObligatorios()

def CreditosSemestre():
    #print("Eligio Creditos de Semestre")
    print("espere...")
    time.sleep(2)
    Funciones.CreditosSemestre()

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
        if menuGestionar == "1": #Listar: Deberá mostrar en consola la lista de los cursos cargados en memoria
            print("Lista de Todos los Cursos")
            Listar()
        elif menuGestionar == "2": #Mostrar: Solicita un código de curso y muestra el detalle del curso
            print("Mostrar Curso")
            Mostrar()
        elif menuGestionar == "3": #Agregar: Permite ingresar un curso manualmente.
            print("Agregar Curso")
            Agregar()
        elif menuGestionar =="4": #Editar: Solicita un código para modificar la información de un curso cargado en memoria.
            print("Modificar Curso")
            Editar()
        elif menuGestionar =="5": #Eliminar: Solicita el código del curso para eliminarlo.
            print("Eliminar Curso")
            Eliminar() 
        elif menuGestionar =="6":
            time.sleep(1)
            break
        else:
            print("Seleccione una opcion valida: ")
            time.sleep(2)

def ConteoCreditos():
    while True:
        os.system('cls')
        print("------------Conteo de Creditos------------")
        print("\t1 - Creditos Aprobados ")
        print("\t2 - Creditos Cursando ")
        print("\t3 - Creditos Pendientes ")
        print("\t4 - Creditso Obligatorios hasta el semestre que desea")
        print("\t5 - Creditos del Semestre")
        print("\t6 - Regresar")
        menuConteo = input("Seleccione una opcion: ")
        if menuConteo=="1":
            print("-------Creditos Aprobados--------")
            CreditosAprobados()
        elif menuConteo=="2":
            print("-------Creditos Cursando--------")
            CreditosCursando()
        elif menuConteo=="3":
            print("-------Creditos Pendientes--------")
            CreditosPendientes()
        elif menuConteo=="4":
            print("-------Creditos Obligatorios hasta el semestre que desea--------")
            CreditosObligatorios()
        elif menuConteo=="5":
            print("-------Creditos del Semestre--------")
            CreditosSemestre()
        elif menuConteo == "6":
            time.sleep(1)
            break
        else:
            print("Seleccione una opcion valida: ")
            time.sleep(2)

#Gest()