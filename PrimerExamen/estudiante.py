import statistics

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre=nombre
        self.notas=notas
    def promedio1(self):
        suma = 0
        for nota in self.notas:
            suma += nota
        promedio = suma / 6
        return promedio
    def promedio2(self):
        promedio = sum(self.notas)/len(self.notas)
        return promedio
    def promedio3(self):
        promedio = statistics.mean(self.notas)
        return promedio


est1 = Estudiante("Jose", [100, 90, 80, 90, 80, 100])
print(est1.promedio1())
print(est1.promedio2())
print(est1.promedio3())


