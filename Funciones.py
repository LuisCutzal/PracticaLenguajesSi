import Cursos
import time
curso=list()

def Listar(): #lista todos los cursos cargados en el sistema
    print("Listar")
    for LisCurso in curso:
        print("[",LisCurso.getCodigo(),",",LisCurso.getNombre(),",",LisCurso.getPrerrequisitos(),",",LisCurso.getOpcionalidad()
        ,",",LisCurso.getSemestre(),",",LisCurso.getCreditos(),",",LisCurso.getEstado(), "]")
        print("-------------------------")
    time.sleep(2)

def Eliminar(): #elimina curso por cusrso a travez del codigo unico
    print("Eliminar")
    idElim=input("Codigo del curso:")
    #banderaE = False
    posicion =0
    while posicion<len(curso):
        if curso[posicion].getCodigo==idElim:
            
        else:
            posicion = posicion + 1
    print(curso)
    time.sleep(3)

def Modificar(): #modifica curso por curso a travez del codigo unico 
    print("Modificar")
    idModif=input("Codigo del Curso: ")
    for LisCurso in curso:
        if LisCurso.getCodigo()== idModif :
            modifNombre=input("Ingrese Nombre del Curso: ")
            LisCurso.setNombre(modifNombre)
            modifPre=input("Ingrese Prerrequisitos del Curso: ")
            LisCurso.setPrerrequisitostos(modifPre)
            modifOpcion=input("Ingrese Opcionallidad del Curso: ")
            LisCurso.setOpcionalidad(modifOpcion)
            modifSemestre=input("Ingrese Semestre del Curso: ")
            LisCurso.setSemestre(modifSemestre)
            modifCreditos=input("Ingrese Creditos del Curso: ")
            LisCurso.setCreditos(modifCreditos)
            modifEstado=input("Ingrese Estado del Curso: ")
            LisCurso.setEstado(modifEstado)
            print("[", LisCurso.getCodigo() , "," , LisCurso.getNombre() , ",", LisCurso.getPrerrequisitos() ,
             ",", LisCurso.getOpcionalidad() , ",", LisCurso.getSemestre() , ",", LisCurso.getCreditos() , ",", LisCurso.getEstado() , "]")
            

def Agregar(): #agrega cursos manualmente
    codigo= input("Codigo del curso: ")
    nombre= input("Nombre del curso: ")
    prerrequisitos= input("Prerrequisitos del curso: ")
    opcionalidad = input("Opcionalidad del curso: ")
    semestre = input("Semestre del Curso: ")
    creditos = input("Creditos del curso: ")
    estado = input("Estado del curso: ")
    curso.append(Cursos.Cursos(codigo,nombre,prerrequisitos,opcionalidad,semestre,creditos,estado))
    print("[", codigo , "," , nombre , ",", prerrequisitos , ",", opcionalidad , ",", semestre , ",", creditos , ",", estado , "]")
    input("Presione Enter para regresar al menu anterior")
            

def Mostrar(): #muestra curso por curso a travez del codigo unico 
    print("Mostrar Curso")
    idMostrar=input("Codigo del Curso: ")
    bandera =False
    for LisCurso in curso:
        if LisCurso.getCodigo()== idMostrar :
            print("[", LisCurso.getCodigo() , "," , LisCurso.getNombre() , ",", LisCurso.getPrerrequisitos() ,
            ",", LisCurso.getOpcionalidad() , ",", LisCurso.getSemestre() , ",", LisCurso.getCreditos() , ",", LisCurso.getEstado() , "]")
            bandera = True
            time.sleep(2)

    if bandera == False:
        input("No existe ese curso, Enter para regresar: ")
    time.sleep(2)
