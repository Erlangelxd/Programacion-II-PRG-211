class Profesor:
    def __init__(self, nombre, profesion):
        self.nombre = None
        self.profesion = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.profesion = input("Profesion: ")
    def mostrar(self):
        print(f"Nombre: {self.nombre}, \n Profesion: {self.profesion}")
    def enseñar(self, Estudiante):  
        print(f"El profesor: {self.nombre} de profesión {self.profesion}, enseña a {Estudiante.nombre} cuyo CI, es {Estudiante.ci}")

class Estudiante:
    def __init__(self):
        self.ci = None
        self.nombre = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.ci = input("CI: ")
    def mostrar(self):
        print(f"Nombre: {self.nombre} \n CI: {self.ci}")

profe1 = Profesor()
est1 = Estudiante()
profe1.leer()
est1.leer()
profe1.enseñar(est1)