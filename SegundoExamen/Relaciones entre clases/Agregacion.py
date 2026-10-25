class Estudiante:
    def __init__(self):
        self.ci = None
        self.nombre = None
    def leer(self):
        self.ci = input("CI: ")
        self.nombre = input("Nombre: ")
    def mostrar(self):
        print(f"Nombre: {self.nombre} ci: {self.ci}")

class Materia:
    def __init__(self):
        self.sigla = None
        self.nombre = None
        self.estudiantes = []
    def leer(self):
        self.sigla = input("Sigla: ")
        self.nombre = input("Nombre de la materia: ")
    def mostrar(self):
        print(f"Sigla: {self.sigla} nombre: {self.nombre}")
    def mostrarEstudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
    def inscribirEst(self, estudiante):
        self.estudiantes.append(estudiante)

materia1 = Materia()
materia1.leer()
while True:
    opcion = input("Opcion: ")
    if opcion == "a":
        estn = Estudiante()
        estn.leer()
        materia1.inscribirEst(estn)
    elif opcion == "b":
        materia1.mostrarEstudiantes()
    elif opcion == "c":
        break
    else:
        print("No valido")