class Animal:
    def __init__(self):
        self.nombreGenerico = None
        self.raza = None
        self.genero = None
        self.edad = None
    def leer(self):
        self.nombreGenerico = input("Nombre generico: ")
        self.raza = input("raza: ")
        self.genero = input("genero: ")
        self.edad = int(input("edad: "))
    def mostrar(self):
        return(f"Nombre: {self.nombreGenerico}")

class Domestico(Animal):
    def __init__(self):
        super().__init__()
        self.nombre = None
        self.nombreDueno = None
    def leer(self):
        super().leer()
        self.nombre = input("Nombre del animal domestico: ")
        self.nombreDueno = input("Nombre del dueño: ")
    def mostrar(self):
        print(f"Nombre: {self.nombre}, dueño: {self.nombreDueno}")

class Silvestre(Animal):
    def __init__(self):
        super().__init__()
        self.habitad = None
    def leer(self):
        super().leer()
        self.habitad = input("Habitad: ")
    def mostrar(self):
        print(f"Habitad: {self.habitad}")

class Gato(Domestico):
    def __init__(self):
        super().__init__()
        self.estadoGarras = None
    def leer(self):
        super().leer()
        self.estadoGarras = input("Estado Garras: ")
    def __str__(self):
        return(f"Nombre: {self.nombre}, genero: {self.genero}, edad: {self.edad}, garras: {self.estadoGarras}")

class Perro(Domestico):
    def __init__(self):
        super().__init__()
        self.potenciaLadrido = None
    def leer(self):
        super().leer()
        self.potenciaLadrido = input("Potencia del ladrido: ")
    def __str__(self):
        return (f"Nombre: {self.nombre}, genero: {self.genero}, edad: {self.edad}, ladrido: {self.potenciaLadrido}")

class Loro(Silvestre):
    def __init__(self):
        super().__init__()
        self.tamanoPico = None
    def leer(self):
        super().leer()
        self.tamanoPico = input("Tamaño del pico: ")
    def __str__(self):
        return (f"Nombre: {self.nombre}, genero: {self.genero}, edad: {self.edad}, pico: {self.tamanoPico}")


gato1 = Gato()
perro1 = Perro()
loro1 = Loro()
loro2 = Loro()
gato1.leer()
perro1.leer()
loro1.leer()
loro2.leer()

if gato1.edad > perro1.edad and gato1.edad > loro1.edad:
    print(gato1)
elif perro1.edad > gato1.edad and perro1.edad > loro1.edad:
    print(perro1)
else:
    print(loro1)

if loro1.genero == "Macho" and loro2.genero == "Macho":
    if loro1.tamanoPico > loro2.tamanoPico:
        print(loro1)
    elif loro1.tamanoPico == loro2.tamanoPico:
        print(loro1)
        print(loro2)
    else:
        print(loro2)
else:
    print("Alguno es hembra")

