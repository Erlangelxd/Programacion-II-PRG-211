def crea():
    with(open("lista_estudiantes.txt", "w")) as archivo:
        archivo.write(" ")

def añadir_en_lista():
    with(open("lista_estudiantes.txt", "a")) as archivo:
        nombre = input("Nombre: ")
        ci = input("CI: ")
        ru = input("RU: ")
        archivo.write(f"{nombre}, {ci}, {ru} \n")

def asistencias():
    with(open("lista_estudiantes.txt", "r")) as archivo:
        contador = 0
        for linea in archivo:
            contador += 1
        print(f"Asistieron {contador} personas")

añadir_en_lista()
añadir_en_lista()

asistencias()
