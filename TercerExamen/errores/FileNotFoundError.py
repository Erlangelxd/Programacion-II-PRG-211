try:
    with(open("xd.py", "r")) as archivo:
        for linea in archivo:
            print(linea)
except FileNotFoundError:
    print("El archivo no existe")