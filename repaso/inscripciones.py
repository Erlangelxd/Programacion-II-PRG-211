class Persona:
    def __init__(self):
        self.__nombre = None
        self.__ci = None
        self.__edad = None
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getCi(self):
        return self.__ci
    def setCi(self, ci):
        self.__ci = ci
    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad = edad
    def leer(self):
        self.setNombre(input("Nombre: "))
        self.setEdad(int(input("Edad: ")))
        self.setCi(input("CI: "))

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.__ru = None
        self.__semestre = None
    def getRU(self):
        return self.__ru
    def setRu(self, ru):
        self.__ru = ru
    def getSemestre(self):
        return self.__semestre
    def setSemestre(self, semestre):
        self.__semestre = semestre
    def leer(self):
        super().leer()
        self.setRu(input("RU: "))
        self.setSemestre(input("Semestre: "))

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.__materia = None
    def getMateria(self):
        return self.__materia
    def setMateria(self, materia):
        self.__materia = materia

class Materia:
    def __init__(self):
        self.nombre = None
        self.inscritos = 0
        self.estudiantes = []
    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)
        self.inscritos += 1
    def mostrarInscritos(self):
        print(self.inscritos)
        for est in self.estudiantes:
            print(est.getNombre())

class Inscripciones:
    def incribirEstudiante(self, materia, estudiante):
        materia.inscribir(estudiante)

est1 = Estudiante()
est2 = Estudiante()
doce1 = Docente()
materia1 = Materia()
ins = Inscripciones()