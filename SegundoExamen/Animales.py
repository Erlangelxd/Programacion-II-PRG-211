class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre
    def hacerSonido(self):
        return "Sonido"
    #getter
    def getNombre(self):
        return self.__nombre
    #setter
    def setNombre(self, otroNombre):
        self.__nombre = otroNombre
    
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza
    def hacerSonido(self):
        return "Guau guau"
    def mostrar(self):
        print(f"Nombre: {self.getNombre()}, raza: {self.getRaza()}")
    def getRaza(self):
        return self.__raza
    def setRaza(self, otraRaza):
        self.__raza = otraRaza

class Loro(Animal):
    def __init__(self, nombre, color_pluma, tipo_pluma):
        super().__init__(nombre)
        self.__color_pluma = color_pluma
        self.__tipo_pluma = tipo_pluma
    def hacerSonido(self):
        return "Pio pio"
    def mostrar(self):
        print(f"Nombre: {self.getNombre()}, color de pluma: {self.getColorPluma()}, tipo de pluma: {self.getTipoPluma()}")
    def getColorPluma(self):
        return self.__color_pluma
    def setColorPluma(self, otroColor):
        self.__color_pluma = otroColor
    def getTipoPluma(self):
        return self.__tipo_pluma
    def setTipoPluma(self, otroTipo):
        self.__tipo_pluma = otroTipo

perro1 = Perro("Max", "Pastor Aleman")
loro1 = Loro("Poli", "verde", "pequeña")
print(perro1.hacerSonido())
print(loro1.hacerSonido())
perro1.mostrar()
loro1.mostrar()
