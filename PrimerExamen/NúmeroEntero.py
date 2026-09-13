class NumeroEntero:
    def __init__(self):
        self.n = None
    def lee(self):
        self.n = int(input("N: "))
    def nroDigStr(self):
        numero = str(self.n)
        return len(numero)
    def nroDigInt(self):
        contador = 0
        n = self.n
        while n > 0:
            digito = n % 10
            contador +=1
            n = n // 10
        return contador
    def primerDig(self):
        numero = str(self.n)
        return numero[0]
    def ultimoDigito(self):
        numero = str(self.n)
        return numero[len(numero)-1]
    def invertir(self):
        numero = str(self.n)
        return numero[::-1]
    def capicua(self):
        if str(self.n) == self.invertir():
            return True
        else:
            return False

nro1 = NumeroEntero()
nro1.lee()
print(nro1.nroDigStr())
print(nro1.nroDigInt())
print(nro1.primerDig())
print(nro1.ultimoDigito())
print(nro1.invertir())
print(nro1.capicua())