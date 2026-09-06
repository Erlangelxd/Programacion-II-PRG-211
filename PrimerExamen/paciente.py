class Paciente:
    def __init__(self):
        self.nombre = None 
        self.peso = None
        self.estatura = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.peso = float(input("Peso: "))
        self.estatura = float(input("Estatura: "))
    def mostrar(self):
        print(f"Nombre: {self.nombre}, peso: {self.peso}, estaura: {self.estatura}")
    def imc(self):
        rimc = self.peso / (self.estatura * self.estatura)
        return rimc
    def resultado(self):
        if self.imc() < 18.49:
            print("Peso bajo")
        elif 18.5 <= self.imc() <= 24.99:
            print("Peso normal")
        elif 25 <= self.imc() <= 29.99:
            print("Sobrepeso")
        elif 30 <= self.imc() <= 34.99:
            print("Obesidad Leve")
        elif 35 <= self.imc() <= 39.99:
            print("Obesidad Media")
        elif self.imc() > 40:
            print("Obesidad Morbida")    
        
paciente1 = Paciente()
paciente1.leer()
paciente1.mostrar()
paciente1.resultado()
    
        