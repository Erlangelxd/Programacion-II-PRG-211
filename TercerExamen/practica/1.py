def tareas():
    Vtereas = []
    n = int(input("N: "))
    for i in range(n):
        tarea = input("Tarea: ")
        Vtereas.append(tarea)
    return Vtereas

def almacenar(tareas, archivo):
    with(open(archivo, "a")) as file:
        for tarea in tareas:
            file.write(f"{tarea}\n")

def crear(archivo):
    with(open(archivo, "w")) as file:
        pass

def abrir(archivo):
    with(open(archivo, "r")) as file:
        for linea in file:
            print(linea)


archivo = "/home/erlan/Escritorio/tareas.txt"
crear(archivo)
almacenar(tareas(), archivo)
abrir(archivo)