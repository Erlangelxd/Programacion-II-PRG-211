class Motor:
    def __init__(self):
        self.marca = None
        self.potencia = None
    def leer(self):
        self.marca = input("Marca: ")
        self.potencia = int(input("Potencia: "))

class Volante:
    def __init__(self):
        self.radio = None
    def leer(self):
        self.radio = float(input("Radio: "))

class Auto:
    def __init__(self):
        self.marca = None
        self.motor = Motor()
        self.volante = Volante()
    def leer(self):
        self.marca = input("Marca Auto: ")
        self.motor.leer()
        self.volante.leer()
    def __str__(self):
        return f"Marca: {self.marca}, potencia del motor: {self.motor.potencia}"

auto = Auto()
auto.leer()
print(auto)