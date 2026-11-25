def mostrar_errores():
    with(open("/home/erlan/Documentos/Programacion-II-PRG211/TercerExamen/practica/servidorlog.txt", "r")) as archivo:
        c = 0
        for linea in archivo:
            V = linea.split(" ")
            if V[0] == "ERROR":
                c += 1
                print(linea)
        print(f"Se encontraron {c} errores")
        
mostrar_errores()
        