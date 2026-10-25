class CuentaBanco:
    def __init__(self, nombre, ci, pin, saldo):
        self.__nombre = nombre
        self.__ci = ci
        self.__pin = pin
        self.__saldo = saldo
    def getNombre(self):
        return self.__nombre
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, monto):
        self.__saldo = monto
    def motrar(self):
        print(f"Cuenta: {self.getNombre()}, Saldo disponible: {self.getSaldo()}")
    def retirarDinero(self, monto):
        total = self.getSaldo() - monto
        self.setSaldo(total)
        print(f"Se retiró {monto} Bs")
    def agregarDinero(self, monto):
        total = self.getSaldo() + monto
        self.setSaldo(total)
        print(f"Se agregó {monto} Bs")

cuenta = CuentaBanco("Erlan", 12345, 1234, 1000)
cuenta.motrar()
cuenta.retirarDinero(500)
cuenta.agregarDinero(5)
cuenta.motrar()