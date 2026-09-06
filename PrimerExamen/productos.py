class Producto:
    def __init__(self):
        self.codigo = None
        self.nombre = None
        self.precio = None
        self.stock = None
    def leer(self):
        self.codigo = input("Codigo: ")
        self.nombre = input("Nombre: ")
        self.precio = float(input("Precio: "))
        self.stock = int(input("Stock: "))
    def mostrar(self):
        print(f"Codigo: {self.codigo}, nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock}")
    def precioDolares(self):
        conversion = self.precio / 11.65
        print(f"El total del producto es {self.precio} Bs, en dolares: {conversion}")


p1 = Producto()
p1.leer()
p1.mostrar()
p1.precioDolares()