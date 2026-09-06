class Estudiante:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.fechaNacimiento = None
        self.genero = None
    def leer(self):
        self.ci = input("CI: ")
        self.nombre = input("Nombre: ")
        self.fechaNacimiento = input("Fecha: ")
        self.genero = input("Genero")
    def mostrar(self):
        print(f"CI: {self.ci}, nombre: {self.nombre}, nacimiento: {self.fechaNacimiento}, genero: {self.genero}")
    def calcularEdad(self):
        añoNacimiento = int(self.fechaNacimiento[6:10])
        edad = 2026 - añoNacimiento
        print(f"{self.nombre} tiene {edad} años")
        return edad
    def compararEdad(self, Estudiante):
        if self.calcularEdad() > Estudiante.calcularEdad():
            print("Yo soy mayor de edad")
        else:
            print("El es mayor de edad")




est1 = Estudiante()
est2 = Estudiante()
est1.leer()
est2.leer()
est1.calcularEdad()
est2.calcularEdad()
est1.compararEdad(est2) 