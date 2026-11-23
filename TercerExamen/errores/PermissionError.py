try:
    with(open("/root/ejemplo.txt", "r")) as archivo:
        for linea in archivo:
            print(linea)
except PermissionError:
    print("No tienes los permisos")