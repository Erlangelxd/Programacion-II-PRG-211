class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    def saludar(self):
        print(f"Hola")

class Ingeniero(Persona):
    def __init__(self, nombre, edad, genero, salario, altura):
        super().__init__(nombre, edad, genero) #No tocar
        self.salario = salario
        self.altura = altura
    def programar(self, lenguaje):
        print(f"Programando en {lenguaje}")
    def resolverEjercicios(self):
        print(f"Resolviendo")
    def saludar(self):
        print(f"Hola soy el/la ing {self.nombre}")

class Medico(Persona):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad = especialidad
    def operar(self):
        print("Operando")
    def saludar(self):
        print(f"Hola soy el/la Lic {self.nombre}")

ing1 = Ingeniero("Erlan", 21, "Masculino", 3000, 165)
med1 = Medico("Luz", 21, "Femenino", "Cardiologia")
med1.operar()
med1.saludar()
