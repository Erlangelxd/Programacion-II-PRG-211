class Empleado:
    def __init__(self):
        self.nombre = None
        self.sueldo = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.sueldo = float(input("Sueldo: "))
    def __str__(self):
        return f"Nombre: {self.nombre}, sueldo: {self.sueldo}"
    def calcularBono(self):
        pass

class Gerente(Empleado):
    def __init__(self):
        super().__init__()
        self.areaDepart = None
    def leer(self):
        super().leer()
        self.areaDepart = input("Area departamento: ")
    def calcularBono(self):
        bono = self.sueldo * 0.5
        return bono

class Programador(Empleado):
    def __init__(self):
        super().__init__()
        self.lenguajes = None
    def leer(self):
        super().leer()
        self.lenguajes = input("Lenguajes: ")
    def calcularBono(self):
        bono = self.sueldo * 0.4
        return bono

class Vendedor(Empleado):
    def __init__(self):
        super().__init__()
        self.totalVentas = None
    def leer(self):
        super().leer()
        self.totalVentas = int(input("Ventas: "))
    def calcularBono(self):
        bono = self.sueldo * 0.3
        return bono

gerente1 = Gerente()
programador1 = Programador()
vendedor1 = Vendedor()
gerente1.leer()
programador1.leer()
vendedor1.leer()
print(gerente1.calcularBono())
print(programador1.calcularBono())
print(vendedor1.calcularBono())