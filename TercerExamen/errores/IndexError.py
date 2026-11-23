try:
    indice = int(input("I: "))
    notas = [30, 30, 40]
    print(notas[indice])
except IndexError:
    print("La posicion no existe")