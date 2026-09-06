class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def area(self):
        area = self.ancho * self.alto
        return area
    def perimetro(self):
        perimetro = 2*(self.alto + self.ancho)
        return perimetro

fig1 = Rectangulo(10, 4)
print(fig1.area())
print(fig1.perimetro())
