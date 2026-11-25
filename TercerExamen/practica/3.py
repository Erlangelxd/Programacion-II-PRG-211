class Jugador:
    def __init__(self, apellido, nombre, edad, peso):
        self.apellido = apellido
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    def __str__(self):
        return f"{self.apellido},{self.nombre},{self.edad},{self.peso}"

def crear(archivo):
    with(open(archivo, "w")) as file:
        file.write(f"Apellido, Nombre, edad, peso\n")

def guardar(archivo):
    with(open(archivo, "a")) as file:
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        peso = input("Peso: ")
        jugador = Jugador(apellido, nombre, edad, peso)
        file.write(f"{jugador}\n")

def mostrar(archivo):
    with(open(archivo, "r")) as file:
        for linea in file:
            print(linea, end=" ")

def buscar_por_apellido(archivo):
    with(open(archivo, "r")) as file:
        Bapellido = input("Apellido: ")
        for linea in file:
            V = linea.strip().split(",")
            if Bapellido.upper() == V[0].upper():
                print(linea)

def buscar_por_nombre(archivo):
    with(open(archivo, "r")) as file:
        Bnombre = input("Nombre: ")
        for linea in file:
            V = linea.strip().split(",")
            if Bnombre.upper() == V[1].upper():
                print(linea)

def peso_total(archivo):
    with(open(archivo, "r")) as file:
        try:
            total = 0
            for linea in file:
                V = linea.strip().split(",")
                if V[3] != "peso":
                    total += int(V[3])
            print(total)
        except ValueError:
            pass

archivo = "/home/erlan/Documentos/Programacion-II-PRG211/TercerExamen/practica/jugadores.txt"
# crear(archivo)
# guardar(archivo)
# mostrar(archivo)
# buscar_por_apellido(archivo)
# buscar_por_nombre(archivo)
# peso_total(archivo)