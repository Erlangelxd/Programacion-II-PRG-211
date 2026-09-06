class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def main():
    estudiantes = []
    while True:
        opcion = input("Opcion: ")
        if opcion == "a":
            nombre = input("Dame un nombre: ")
            edad = int(input("Dame la edad: "))
            estudiante = Estudiante(nombre, edad)
            estudiantes.append(estudiante)
        elif opcion == "b":
            for estudiante in estudiantes:
                if estudiante.edad < 20:
                    print(estudiante.nombre)
        elif opcion == "c":
            try:
                sumaNotas = 0
                for estudiante in estudiantes:
                    sumaNotas += estudiante.edad
                nroEstudiantes = len(estudiantes)
                promedio = sumaNotas / nroEstudiantes
                print(promedio)
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
                pass

main()