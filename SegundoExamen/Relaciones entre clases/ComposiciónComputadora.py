class Procesador:
    def __init__(self):
        self.marca = None
        self.velocidad = None
    def leer(self):
        self.marca = input("Marca procesador: ")
        self.velocidad = float(input("Velocidad procesador: "))
    def mostrar(self):
        print(f"Marca: {self.marca}, velocidad = {self.velocidad}")

class Memoria:
    def __init__(self):
        self.capacidad = None
    def leer(self):
        self.capacidad = float(input("Capacidad Memoria: "))
    def mostrar(self):
        print(f"capacidad: {self.capacidad}")

class Computadora:
    def __init__(self):
        self.marca = None
        self.color = None
        self.memoria = Memoria()
        self.procesador = Procesador()
    def leer(self):
        self.marca = input("Marca de computadora: ")
        self.color = input("Color de la computadora")
        self.memoria.leer()
        self.procesador.leer()
    def mostrar(self):
        print(f"Marca: {self.marca} color: {self.color} procesador: {self.procesador.marca} velocidad: {self.memoria.capacidad}")


pc1 = Computadora()
pc2 = Computadora()

pc1.leer()
pc2.leer()

if pc1.marca == pc2.marca:
    print("Son de la misma marca")
else:
    print("Son de distintas marcas")

if pc1.memoria.capacidad > pc2.memoria.capacidad:
    print(pc1.mostrar())
else:
    print(pc2.mostrar())