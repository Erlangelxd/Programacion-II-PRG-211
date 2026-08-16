class Persona:
    def __init__(self, nombre, edad, altura, color, nacionalidad, genero, ci):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.color = color
        self.nacionalidad = nacionalidad
        self.genero = genero
        self.ci = ci
    def saludar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")
    def comer(self):
        print(f"Estoy comiendo")
    def dormir(self):
        print(f"Durmiendo")
    def trabajar(self):
        print(f"Trabajando")

