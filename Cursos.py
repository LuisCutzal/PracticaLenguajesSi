#ClassCursos es la cvlase que genera los objetos que seran parte de la lista
class Cursos(object):
    """codigo =0
    nombre=""
    prerrequisitos=0
    opcionalidad=0
    semestre=0
    creditos=0
    estado=0"""
#---------------------------metodos-----------------------------------------------
    def __init__ (self, codigo, nombre, prerrequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo=codigo
        self.nombre=nombre
        self.prerrequisitos=prerrequisitos #[] colocar esto luego
        self.opcionalidad=opcionalidad
        self.semestre=semestre
        self.creditos=creditos
        self.estado=estado

#---------------get----------------
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getPrerrequisitos(self):
        return self.prerrequisitos

    def getOpcionalidad(self):
        return self.opcionalidad

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos

    def getEstado(self):
        return self.estado

#-----------set------------
    def setCodigo(self, nuevoCodigo):
        self.codigo=nuevoCodigo

    def setNombre(self, nuevoNombre):
        self.nombre=nuevoNombre

    def setPrerrequisitos(self, nuevoPrerrequisitos):
        self.prerrequisitos=nuevoPrerrequisitos

    def setOpcionalidad(self, nuevoOpcionalidad):
        self.opcionalidad=nuevoOpcionalidad

    def setSemestre(self, nuevoSemestre):
        self.semestre=nuevoSemestre

    def setCreditos(self, nuevoCreditos):
        self.creditos=nuevoCreditos

    def setEstado(self, nuevoEstado):
        self.estado=nuevoEstado
    

    def __str__(self):
        return (self.codigo, self.nombre, self.prerrequisitos, self.opcionalidad, self.semestre, self.creditos, self.estado)
