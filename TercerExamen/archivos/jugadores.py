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
        pass

def agregar(archivo):
    with(open(archivo, "a")) as file:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        peso = input("Peso: ")
        jugador = Jugador(apellido, nombre, edad, peso)
        file.write(f"{jugador}\n")

def buscar_por_apellido(archivo):
    with(open(archivo, "r")) as file:
        apellido = input("Apellido: ")
        for linea in file:
            V = linea.strip().split(",")
            if V[0] == apellido:
                print(linea)

def buscar_por_nombre(archivo):
    with(open(archivo, "r")) as file:
        nombre = input("Nombre: ")
        for linea in file:
            V = linea.strip().split(",")
            if V[1] == nombre:
                print(linea)

def peso_total(archivo):
    with(open(archivo, "r")) as file:
        total = 0
        for linea in file:
            V = linea.strip().split(",")
            total += int(V[3])
    print(f"Peso total es: {total}")

def main():
    archivo = "./TercerExamen/archivos/jugadores.txt"
    # crear(archivo)
    # agregar(archivo)
    # agregar(archivo)
    # agregar(archivo)
    buscar_por_apellido(archivo)
    buscar_por_nombre(archivo)
    peso_total(archivo)

if __name__ == "__main__":
    main()