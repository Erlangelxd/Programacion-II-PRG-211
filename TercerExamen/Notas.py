class Archivo:
    def __init__(self, archivo):
        self.archivo = archivo
    def crear(self):
        with(open(self.archivo, "w")) as archivo:
            pass
    def insertar_notas(self):
        with(open(self.archivo, "a")) as archivo: 
            nombre = input("Nombre: ")
            n1 = input("Nota 1: ")
            n2 = input("Nota 2: ")
            n3 = input("Nota 3: ")
            archivo.write(f"{nombre},{n1},{n2},{n3}\n")
    def estado(self):
        with(open(self.archivo, "r")) as archivo:
            for linea in archivo:
                V = linea.strip().split(",")
                total = int(V[1]) + int(V[2]) + int(V[3])
                if total >= 51:
                    print(f"{V[0]} aprobó")
                elif total >= 40 and total < 51:
                    print(f"{V[0]} va para el 2T")
                elif total < 40:
                    print(f"{V[0]} reprobó")

try:
    notas = Archivo("./TercerExamen/Finales.txt")
    notas.borrar()
except AttributeError:
    print("El metodo no existe")        