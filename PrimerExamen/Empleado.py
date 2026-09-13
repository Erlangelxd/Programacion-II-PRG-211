from datetime import date
class Empleado:
    def __init__(self):
        self.ci = None
        self.nombre = None
        self.fechaNacimiento = None
        self.fechaIngreso = None
        self.salario = None
    def leer(self):
        self.ci = input("CI: ")
        self.nombre = input("Nombre: ")
        año = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Dia: "))
        self.fechaNacimiento = date(año, mes, dia)
        año = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Dia: "))
        self.fechaIngreso = date(año, mes, dia)
        self.salario = float(input("Salario: "))
    def edadParaAño(self):
        año = self.fechaNacimiento[6:10]
        edad = 2026 - int(año)
        return edad
    def edadDate(self):
        hoy = date.today()
        edad = hoy.year - self.fechaNacimiento.year
        cumpleañosPendiente = (hoy.month, hoy.today) < (self.fechaNacimiento.month, self.fechaNacimiento.day)
        if cumpleañosPendiente:
            edad = edad - 1
        return edad
    def antiguedad(self):
        hoy = date.today()
        años = hoy.year - self.fechaIngreso.year
        return años
    def bono(self):
        self.salario += (self.salario)*0.02 * self.antiguedad()
    def compararSalario(self, compañero):
        if self.salario > compañero.salario:
            print(f"{self.nombre} gana mas dinero") 
        else:
            print(f"{compañero.nombre} gana mas dinero")

per1 = Empleado()
per2 = Empleado()
per1.leer()
per2.leer()
per2.bono()
per1.compararSalario(per2)

        