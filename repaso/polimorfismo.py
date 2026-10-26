class Ingeniero:
    def __init__(self):
        self.nombre = None
        self.ci = None
        self.experiencia = None
        self.sueldo = None
    def leer(self):
        self.nombre = input("Nombre: ")
        self.ci = input("CI: ")
        self.experiencia = int(input("Experiencia: "))                
        self.sueldo = float(input("Sueldo: "))
    def contruir(self):
        pass

class Sistemas(Ingeniero):
    def __init__(self):
        super().__init__()   
        self.lenguajeProgramacion = None
    def leer(self):
        super().leer()
        self.lenguajeProgramacion = input("Lenguaje: ")
    def contruir(self):
        return f"Contruyendo la aplicacion web"

class Civil(Ingeniero):
    def __init__(self):
        super().__init__()
        self.especialidad = None
    def leer(self):
        super().leer()
        self.especialidad = input("Especialidad: ")
    def contruir(self):
        return f"Contruyendo estructura"

sist = Sistemas()
civil = Civil()

sist.leer()
civil.leer()

print(sist.contruir())
print(civil.contruir())