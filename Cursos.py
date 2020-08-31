#ClassCursos es la cvlase que genera los objetos que seran parte de la lista
class Cursos(object):

#---------------------------metodos-----------------------------------------------
    def __init__ (self, codigo, nombre, prerrequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo=codigo
        self.nombre=nombre
        self.prerrequisitos=prerrequisitos  
        self.opcionalidad=opcionalidad
        self.semestre=semestre
        self.creditos=creditos
        self.estado=estado
    
#---------------get----------------
    def getCodigo(self):
        return str(self.codigo)

    def getNombre(self):
        return str(self.nombre)

    def getPrerrequisitos(self):
        return self.prerrequisitos

    def getOpcionalidad(self):
        return int(self.opcionalidad)

    def getSemestre(self):
        return (self.semestre)

    def getCreditos(self):
        return int(self.creditos)

    def getEstado(self):
        return int(self.estado)

#-----------set------------
    def setCodigo(self, nuevoCodigo):
        self.codigo=str(nuevoCodigo)

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

    def APrep(self, Aprep):
        self.prerrequisitos.push(Aprep)



    def __str__(self):
        return (self.codigo, self.nombre, self.prerrequisitos, self.opcionalidad, self.semestre, self.creditos, self.estado)
