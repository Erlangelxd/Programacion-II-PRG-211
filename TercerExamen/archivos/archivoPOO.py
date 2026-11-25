class Archivo:
    def __init__(self, archivo):
        self.archivo = archivo
    def crear(self):
        with(open(self.archivo, "w")) as archivo:
            pass
    def registrarse(self):
        with(open(self.archivo, "a")) as archivo:
            nombre = input("Nombre: ")
            ci = input("Ci: ")
            ru = input("RU: ")
            edad = input("Edad: ")
            archivo.write(f"{nombre},{ci},{ru},{edad}\n")
    def menores(self):
        with(open(self.archivo, "r")) as archivo:
            for linea in archivo:
                V = linea.strip().split(",")
                if int(V[3]) < 18:
                    print(linea, end=" ")


lista = Archivo("./TercerExamen/listaEstudiantes.txt")
# lista.crear()
# lista.registrarse()
# lista.registrarse()
lista.menores()