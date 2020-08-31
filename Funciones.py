import Cursos
import time
global curso
curso=list()
#prerrequisitos=list()
def Listar(): #lista todos los cursos cargados en el sistema
    print("Listar")
    for LisCurso in curso:
        AgrePre=""
        if LisCurso.getPrerrequisitos != "":
            if LisCurso.getPrerrequisitos(): #ver
                for Obtener in LisCurso.getPrerrequisitos():
                    #AgrePre=AgrePre+(LisCurso.getPrerrequisitos()[range])
                    #AgrePre+str(Obtener)
                    AgrePre=AgrePre+str(Obtener)
                    AgrePre=AgrePre +";"
                    #print(LisCurso.getPrerrequisitos()[range])
            AgrePre=AgrePre[:-1]
            print("[",LisCurso.getCodigo(),",",LisCurso.getNombre(),",",AgrePre,",",LisCurso.getOpcionalidad()
            ,",",LisCurso.getSemestre(),",",LisCurso.getCreditos(),",",LisCurso.getEstado(), "]")
        else:
            #agrepre-=1
            print("[",LisCurso.getCodigo(),",",LisCurso.getNombre(),",",LisCurso.getPrerrequisitos(),",",LisCurso.getOpcionalidad()
            ,",",LisCurso.getSemestre(),",",LisCurso.getCreditos(),",",LisCurso.getEstado(), "]")
        print("-------------------------")
    input("Presione enter para regresar al menu anterior: ")

def Eliminar(): #elimina curso por cusrso a travez del codigo unico
    print("Eliminar")
    idElim= input("Codigo del curso: ")
    banderaE = False
    prueba = 0
    for recor in range(len(curso)):
        if idElim == curso[recor].getCodigo():
            prueba = recor
            banderaE = True
    if banderaE !=True:
        input("El curso no existe ")
    else:
        curso.pop(prueba)
        input("Curso eliminado, presione enter para regresar: ")
        
def Modificar(): #modifica curso por curso a travez del codigo unico 
    print("Modificar")
    idModif=input("Codigo del Curso: ")
    for LisCurso in curso:
        if LisCurso.getCodigo()== idModif :
            #modificar nombre----------------------------------
            Mo_Nom = input("¿Quiere modificar el nombre del Curso?, [si/no]")
            if Mo_Nom == "si":
                modifNombre=input("Ingrese Nombre del Curso: ")
                LisCurso.setNombre(modifNombre)
            #modificar Prerrequisitos------------------------------
            print()
            Mo_Pre = input("¿Quiere modificar los Prerrequisitos del Curso?, [si/no]")
            if Mo_Pre =="si":
                modifPre=input("Ingrese Prerrequisitos del Curso, si son más de 1 prerrequisito, ingresarlos con punto y coma: ").split(';')
                LisCurso.setPrerrequisitos(modifPre)
            #modificar Opcionalidad--------------------------------
            print()
            Mo_op = input("¿Quiere modificar la Opcionalidad del Curso?, [si/no]")
            if Mo_op=="si":
                modifOpcion=input("Ingrese Opcionallidad del Curso: ")
                LisCurso.setOpcionalidad(modifOpcion)
            #modificar Semestre-------------------------------------
            print()
            Mo_sem = input("¿Quiere modificar el Semestre del Curso?, [si/no]")
            if Mo_sem=="si" or Mo_sem =="SI" or Mo_sem== "Si" or Mo_sem == "sI":
                modifSemestre=input("Ingrese Semestre del Curso: ")
                LisCurso.setSemestre(modifSemestre)
            #modificar Creditos-------------------------------------
            print()
            Mo_credit = input("¿Quiere modificar los Creditos del Curso?, [si/no]")
            if Mo_credit =="si":
                modifCreditos=input("Ingrese Creditos del Curso: ")
                LisCurso.setCreditos(modifCreditos)
            #modificar Estados--------------------------------------
            print()
            Mo_est = input("¿Quiere modificar el Estado del Curso?, [si/no]")
            if Mo_est =="si":
                modifEstado=input("Ingrese Estado del Curso: ")
                LisCurso.setEstado(modifEstado)
            print()
            print("[", LisCurso.getCodigo() , "," , LisCurso.getNombre() , ",", LisCurso.getPrerrequisitos() ,
             ",", LisCurso.getOpcionalidad() , ",", LisCurso.getSemestre() , ",", LisCurso.getCreditos() , ",", LisCurso.getEstado() , "]")
            input("Curso Modificado, presione Enter para regresar: ")

def Agregar(): #agrega cursos manualmente
    codigo= input("Codigo del curso: ")
    nombre= input("Nombre del curso: ")
    prerrequisitos= input("Prerrequisitos del curso: ").split(';')
    opcionalidad = input("Opcionalidad del curso: ")
    semestre = input("Semestre del Curso: ")
    creditos = input("Creditos del curso: ")
    estado = input("Estado del curso: ")
    banderaA = False
    for Areco in range(len(curso)):
        if curso[Areco].getCodigo() == codigo :
            banderaA=True
    if banderaA != True:
        print("Curso agregado con Exito")
        curso.append(Cursos.Cursos(codigo,nombre,prerrequisitos,opcionalidad,semestre,creditos,estado))
        print("[", codigo , "," , nombre , ",", prerrequisitos , ",", opcionalidad , ",", semestre , ",", creditos , ",", estado , "]")
    else: 
        print("Error, Codigo de Curso Existente: ") 
    input("Presione Enter para regresar al menu anterior: ")

def Mostrar(): #muestra curso por curso a travez del codigo unico 
    print("Mostrar Curso")
    idMostrar=input("Codigo del Curso: ")
    bandera =False
    for LisCurso in curso:
        if LisCurso.getCodigo() == idMostrar :
            print("[", LisCurso.getCodigo() , "," , LisCurso.getNombre() , ",", LisCurso.getPrerrequisitos() ,
            ",", LisCurso.getOpcionalidad() , ",", LisCurso.getSemestre() , ",", LisCurso.getCreditos() , ",", LisCurso.getEstado() , "]")
            bandera = True
            time.sleep(2)
    if bandera == False:
        input("No existe ese curso, Enter para regresar: ")
    time.sleep(2)

#------------------------creditos--------------------------

def CreditosAprobados():
    #print("Mostrar Creditos aprobados")
    CreditosA = 0
    for ap in range(len(curso)): #ap es creditos aprobados
        if curso[ap].getEstado() == 0:
            CreditosA = CreditosA+curso[ap].getCreditos()
    print("El total es: " + str(CreditosA))
    input("Presione enter para regresar: ")

def CreditosCursando():
    #print("Creditos Cursando")
    CreditosC= 0
    for cur in range(len(curso)): #cur es creditos cursados
        if curso[cur].getEstado() == 1:
            CreditosC= CreditosC + curso[cur].getCreditos()
    print("El total es: " + str(CreditosC))
    input("Presione enter para regresar: ")

def CreditosPendientes():
    #print("Creditos Pendientes")
    CreditosP=0
    for cp in range(len(curso)): #cp es creditos pendientes
        if curso[cp].getEstado() == -1 and curso[cp].getOpcionalidad() == 1:
            CreditosP= CreditosP + curso[cp].getCreditos()
    print("El total es: " + str(CreditosP))
    input("Presione enter para regresar: ")

def CreditosObligatorios():
    #print("Creditos Obligatorios")
    semestre = input("Ingrese el numero de semestre que quiere consultar: ")
    if semestre >="1" and semestre <="10":
        CreditosS=0
        for co in range(len(curso)): #co es creditos obligatorios
            if curso[co].getOpcionalidad() == 1 and curso[co].getSemestre() <= semestre:
                CreditosS = CreditosS+ curso[co].getCreditos()
        print("Creditos total: " + str(CreditosS))
    else:
        print("No Existe ese semestre ")
    input("Presione enter para regresar: ")

def CreditosSemestre():
    #print("Creditos de cursos Aprobados y Pendientes del Semestre")
    semestre = input("Ingrese el numero de semestre que quiere consultar: ")
    if semestre >= "1" and semestre <="10":
        ap=0 #ap es creditos aprobados
        cp=0 #cp es creditos pendientes
        for i in range(len(curso)):
            if curso[i].getEstado() == 0 and curso[i].getSemestre()== semestre:
                ap=ap+curso[i].getCreditos()
            if curso[i].getEstado()== -1 and curso[i].getSemestre()== semestre:
                cp=cp+curso[i].getCreditos()
        print("Cursos Aprobados: " +str(ap))
        print("Cursos Pendientes: " + str(cp))
    else:
        print("No Existe ese semestre ")
    input("Presione enter para regresar: ")