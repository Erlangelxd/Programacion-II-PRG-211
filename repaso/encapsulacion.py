class Persona:
    def __init__(self):
        self.__nombre = None
        self.__ci = None
        self.__edad = None
    def getNombre(self):
        return self.__nombre
    def getCi(self):
        return self.__ci
    def getEdad(self):
        return self.__edad
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setCi(self, ci):
        self.__ci = ci
    def setEdad(self, edad):
        self.__edad = edad
    def leer(self):
        self.setNombre(input("Nombre: "))
        self.setCi(input("CI: "))
        self.setEdad(int(input("Edad: ")))
    def __str__(self):
        return f"Nombre: {self.getNombre()}, CI: {self.getCi()}"

persona1 = Persona()
persona1.leer()
print(persona1)
persona1.setNombre("Angel")
print(persona1)