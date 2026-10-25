class Estudiante:
    def __init__(self):
        self._ci = None
        self._nombre = None #Protegido
        self._nota = None
    def setCi(self, ci):
        self._ci = ci
    def setNombre(self, nombre):
        self._nombre = nombre
    def setNota(self, nota):
        if 0 <= nota and nota <= 100:
            self._nota = nota
        else:
            print("La nota esta fuera de rango")
    def getCi(self):
        return self._ci
    def getNombre(self):
        return self._nombre
    def getNota(self):
        return self._nota
    def leer(self):
        self.setCi(input("CI: "))
        self.setNombre(input("Nombre: "))
        self.setNota(int(input("Nota: ")))
    def __str__(self):
        return (f"Nombre: {self.getNombre()}, ci: {self.getCi()}, nota: {self.getNota()}")


est1 = Estudiante()
est1.leer()
print(est1)
est1.setNota(100)
print(est1)
est1.setNota(105)
print(est1)