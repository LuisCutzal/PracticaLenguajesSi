import os
import time
import csv
import sys

def Archivos(ruta):   #ubicacion del archivo
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
    input("presione Enter para regresar al menu principal: ")

#print(Archivos('datos/archivo.csv'))

"""def Mando():
    print("Primero")
    valores = contenidio
    lineas = next(valores)
    print("-------Lista---------")
    print(lineas)
"""