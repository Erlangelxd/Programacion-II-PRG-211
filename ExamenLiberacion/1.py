class Estudiante:
    def __init__(self, nombre, edad, semestre, ru, ci):
        self.nombre = nombre 
        self.edad = edad
        self.semestre = semestre
        self.ru = ru
        self.ci = ci
    def __str__(self):
        return f"{self.nombre},{self.edad},{self.semestre},{self.ru},{self.ci}"

def crear_lista(archivo):
    with(open(archivo, "w")) as archivo:
        pass

def agregar_en_lista(archivo):
    with(open(archivo, "a")) as archivo:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        semestre = input("Semestre: ")
        ru = input("RU: ")
        ci = input("CI: ")
        estudiante = Estudiante(nombre, edad, semestre, ru, ci)
        archivo.write(f"{estudiante}\n")

def filtrar_por_semestre(archivo):
    with(open(archivo, "r")) as archivo:
        semestre = input("Semestre: ")
        for linea in archivo:
            V = linea.strip().split(",")
            if V[2] == semestre:
                print(linea, end=" ")

def main():
    crear_lista("estudi.txt")
    agregar_en_lista("estudi.txt")
    agregar_en_lista("estudi.txt")
    filtrar_por_semestre("estudi.txt")

if __name__ == "__main__":
    main()