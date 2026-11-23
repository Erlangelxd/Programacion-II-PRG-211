while True:
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        resultado = a + b
        print(resultado)
    except TypeError, ValueError:
        print("uno de los valores es un str")
    