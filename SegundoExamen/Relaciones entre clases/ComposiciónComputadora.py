class Computadora:
    def __init__(self, marca, color, marcaPro, velocidad, capacidad):
        self.marca = marca
        self.color = color
        self.procesador = Procesador(marcaPro, velocidad) 
        self.memoria = Memoria(capacidad)
    def leer(self):
        self.marca = input("Marca: ")
        self.color = input("Color: ")
    def mostrar(self):
        print(f"Marca: {self.marca} \n color: {self.color}")

class Procesador:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad
    def llenar(self):
        self.marca = input("Marca: ")
        self.velocidad = input("Velocidad: ")
    def mostrar(self):
        print(f"Marca: {self.marca} \n velocidad: {self.velocidad}")

class Memoria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
    def llenar(self):
        self.capacidad = input("capacidad: ")
    def mostrar(self):
        print(f"Capacidad: {self.capacidad}")

pc1 = Computadora("Lenovo", "Negro", "Ryzen", "3200", "512")
pc2 = Computadora("Hp", "Negro", "Intel", "4000", "512")
if pc1.marca == pc2.marca:
    print("Son de la misma marca")
else:
    print("Son de marcas distintas")
if pc1.memoria.capacidad > pc2.memoria.capacidad:
    print(pc1.marca, pc1.memoria.capacidad, pc1.procesador.marca, pc1.procesador.velocidad)
else:
    print(pc2.marca, pc2.memoria.capacidad, pc2.procesador.marca, pc2.procesador.velocidad)