class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def valorTotal(self):
        valor = self.precio * self.cantidad
        print(f"El valor total del producto es: {valor} Bs.")

p1 = Producto("Laptops", 5000, 30)
p1.valorTotal()