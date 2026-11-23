try:
    a = int(input("A: "))
    b = int(input("B: "))
    print(a/b)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
