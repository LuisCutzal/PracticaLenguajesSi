import os
import sys
import time
import Cargar_archivo
import Gestionar_curso
#menu opcion 1
def Op1():
    print("Ha elegido cargar archivo")
    print("espere...")
    time.sleep(2)
    #ruta='datos/archivo.csv'
    Cargar_archivo.Archivos()
    #os.system('cls')
#----------------
#menu opcion 2
def Op2():
    print("Ha elegido Gestionar Cursos")
    print("espere...")
    time.sleep(2)
    Gestionar_curso.Gest()
#----------------
#menu opcion 3
def Op3():
    print("Ha elegido el Conteo de Creditos:")
    print("espere....")
    Gestionar_curso.ConteoCreditos()
#---------------
#menu opcion 4
def Op4():
    print("Ha elegido el Mapa de Cursos:")
    print("espere....")
    
#--------------
def MenuInicio():
    while True:
        os.system('cls')
        print("*****************************")
        print("*****************************")
        print("*****************************")
        print ("Menú Principal")
        print ("\t1 - Cargar archivo de entrada: ")
        print ("\t2 - Gestionar Cursos: ")
        print ("\t3 - Conteo de Creditos: ")
        print ("\t4 - Mapa de Cursos: ")
        print ("\t5 - Salir ")
        print("*****************************")
        print("*****************************")
        print("*****************************")
        opcionMenu = input("Escriba uno de los 5 números a  la que quiere ingresar: ")
        if opcionMenu == "1":
            Op1()
        elif opcionMenu == "2":
            Op2()
        elif opcionMenu=="3":
            Op3()
        elif opcionMenu=="4":
            Op4()
        elif opcionMenu=="5":
            sys.exit(0)
        else:
            print("Ha pusaldo una tecla incorrecta, vuelva a intentarlo")
            time.sleep(2)

def main():
    print("------------Lenguajes Formales y de Programacion-----------")
    print ("Seccion: B")
    print ("Carné: 201700841")
    input("presione cualquier tecla para iniciar el programa: ")
    MenuInicio()

if __name__ == "__main__":
    main()