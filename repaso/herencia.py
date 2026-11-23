class Animal:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.raza = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.raza = input("Raza: ")

class Domestico(Animal):
    def __init__(self):
        super().__init__()
        self.nombreDueño = None
    def leer(self):
        super().leer()
        self.nombreDueño = input("Dueño: ")

class Salvaje(Animal):
    def __init__(self):
        super().__init__()
        self.habitad = None
    def leer(self):
        super().leer()
        self.habitad = input("Habitad: ")

class Gato(Domestico):
    def __init__(self):
        super().__init__()
        self.color = None
    def leer(self):
        super().leer()
        self.color = input("Color: ")
    def __str__(self):
        return f"Nombre: {self.nombre}, color: {self.color}, dueño: {self.nombreDueño}"

class Tilcayo(Salvaje):
    def __init__(self):
        super().__init__()
        self.tamaño = None
    def leer(self):
        super().leer()
        self.tamaño = input("Tamaño: ")
    def __str__(self):
        return f"Nombre: {self.nombre}, tamaño: {self.tamaño}, edad: {self.edad}"

gato1 = Gato()
tilcayo = Tilcayo()

if gato1.edad == tilcayo.edad:
    print(gato1)
else:
    print(tilcayo)