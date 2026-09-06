class CuentaBancaria:
    def __init__(self):
        self.balance = 0
    def depositar(self, monto):
        self.balance += monto
    def retirar(self, monto):
        if self.balance > 0:
            if monto <= self.balance:
                self.balance -= monto
        else:
            print("No tienes dinero")
    def mostrar(self):
        print(f"Saldo: {self.balance} Bs.")

cu = CuentaBancaria()
cu.mostrar()
cu.depositar(2000)
cu.mostrar()
cu.retirar(1000)
cu.mostrar()