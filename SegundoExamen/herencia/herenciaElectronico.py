class ArtefactoElectronico:
    def __init__(self):
        self.marca = None
        self.precio = None
    def leer(self):
        self.marca = input("Marca: ")
        self.precio= input("Precio: ")
    def mostrar(self):
        print(f"Marca: {self.marca} \n Precio: {self.precio}")

class Celular(ArtefactoElectronico):
    def __init__(self):
        super().__init__()
        self.tamPantalla = None
    def leer(self):
        super().leer()
        self.tamPantalla = input("Tamaño de pantalla: ")
    def mostrar(self):
        super().mostrar()
        print(f"Tamaño de pantalla: {self.tamPantalla}")

class Televisor(ArtefactoElectronico):
    def __init__(self):
        super().__init__()
        self.resolucion = None
        self.smart = None
    def leer(self):
        super().leer()
        self.resolucion = input("Resolucion: ")
        self.smart = input("Smart: ")
    def mostrar(self):
        super().mostrar()
        print(f"Resolucion: {self.resolucion}\nSmart: {self.smart}")

class Licuadora(ArtefactoElectronico):
    def __init__(self):
        super().__init__()
        self.rpm = None
        self.potencia = None
    def leer(self):
        super().leer()
        self.rpm = input("RPM: ")
        self.potencia = input("Potencia: ")
    def mostrar(self):
        super().mostrar()
        print(f"RPM: {self.rpm}\n potencia: {self.potencia}")

c1 = Celular()
tv1 = Televisor()
lic1 = Licuadora()
c1.leer()
tv1.leer()
lic1.leer()
c1.mostrar()
tv1.mostrar()
lic1.mostrar()