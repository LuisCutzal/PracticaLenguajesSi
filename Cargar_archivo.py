import os
import time
import csv
import sys
import Cursos
import Funciones


"""def Archivos(ruta):   #ubicacion del archivo
    with open(ruta) as cont: 
        arch = csv.reader(cont)
        linea1 = next(arch) #primera linea del archivo .csv
        print("------ INCIO DEL ARCHIVO -----------")
        print(linea1)
        def Cursos():
            for contenido in arch:
                #contenido de nuestro archivo .csv
                    print(contenido)
        Cursos()
            #print("hola")
        #print("La clase de la estructura es: ")
        #print(type(archivocsv))
        print("------- fin DEL ARCHIVO ------------")
    input("presione Enter para regresar al menu principal: ")"""

def Archivos(): # aun faltan condiciones
    NArchivo= str(input("Ingrese el nombre del archivo de entrada: "))
    archivo=open(NArchivo)
    leer = csv.reader(archivo)
    contador=0
    for tupla in leer:
        Funciones.curso.append(Cursos.Cursos(tupla[0], tupla[1], tupla[2].split(';'), tupla[3], tupla[4], tupla[5], tupla[6]))
    input("Archivo cargado correctamente, Presione enter para regresar: ")
