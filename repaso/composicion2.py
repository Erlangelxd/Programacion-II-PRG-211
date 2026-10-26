class Celular:
    def __init__(self):
        self.marca = None
        self.pantalla = Pantalla()
        self.camara = Camara()
    def leer(self):
        self.marca = input("Marca del celular: ")
        self.pantalla.leer()
        self.camara.leer()
    def __str__(self):
        return f"Marca: {self.marca}, pantalla: {self.pantalla.tamaño}"

class Pantalla:
    def __init__(self):
        self.tamaño = None
        self.resolucion = None
    def leer(self):
        self.tamaño = int(input("Pulgadas: "))
        self.resolucion = input("Resolucion: ")

class Camara:
    def __init__(self):
        self.pixeles = None
    def leer(self):
        self.pixeles = int(input("Pixeles: "))



cel1 = Celular()
cel1.leer()
print(cel1)