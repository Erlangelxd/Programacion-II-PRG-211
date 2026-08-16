class NumeroEspecial:
    def __init__(self, x):
        self.x = x
    def es_capicua(self):
        inversa = str(self.x)[::-1]
        if inversa == str(self.x):
            return 1
        else:
            return 0
    def es_primo(self):
        c = 0
        for i in range(1, self.x +1):
            if self.x % i == 0:
                c+=1
        if c == 2:
            return 1
        else:
            return 0


def main():
    x = int(input("X: "))
    y = int(input("Y: "))
    if y > x:
        for i in range(x, y):
            numero = NumeroEspecial(i)
            if numero.es_capicua() == 1:
                print(f"CAPICUA {i}")
            elif numero.es_primo() == 1:
                print(f"PRIMO {i}")

main()