class Usuario():
    def __init__(self, nombre, edad, contraseña):
        self.nombre = nombre
        self.edad = edad
        self.contraseña = contraseña
    def crecer(self):
        self.edad += 1
    def saludar(self):
        return f"Hola me llamo {self.nombre}"
    def __str__(self):
        return f"{self.nombre}, {self.edad}"

class Usuarios:
    def __init__(self):
        self.V = []
    def añadir(self, usuario):
        self.V.append(usuario)
    def mostrarUsuario(self):
        indice = int(input("Indice: "))
        return self.V[indice]
    
def registro():
    while True:
        try:
            DB = Usuarios()
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            contraseña = input("Contraseña: ")
            usu = Usuario(nombre, edad, contraseña)
            DB.añadir(usu)
            
        except Exception:
            print("Vuelve a intentarlo")

registro()
