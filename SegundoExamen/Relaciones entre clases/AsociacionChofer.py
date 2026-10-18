class Chofer:
    def __init__(self):
        self.ci = None
        self.nombre = None
    def leer(self):
        self.ci = input("CI: ")
        self.nombre = input("Nombre: ")
    def mostrar(self):
        print(f"Nombre: {self.nombre} \n CI: {self.ci}")
    def conduce(self, Taxi):
        print(f"El Chofer: {self.nombre}, conduce el taxi de color {Taxi.color}, con placa {Taxi.placa}")

class Taxi:
    def __init__(self):
        self.placa = None
        self.color = None
    def leer(self):
        self.placa = input("Placa: ")
        self.color = input("Color: ")
    def mostrar(self):
        print(f"Color: {self.color} \n Placa: {self.placa}") 

chofer1 = Chofer()
# taxi1 = Taxi()
chofer1.leer()
# taxi1.leer()
chofer1.mostrar()