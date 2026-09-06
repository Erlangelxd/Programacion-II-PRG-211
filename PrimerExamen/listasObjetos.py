class Paciente:
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
    def imc(self):
        resultado = self.peso / self.altura ** 2
        return resultado

def main():
    pacientes = []
    while True:
        opcion = input("Dame una opcion: ")
        match opcion:
            case "a":
                nombre = input("Dame un nombre: ")
                peso = float(input("Dame el peso: "))
                altura = float(input("Dame la altura: "))
                paciente = Paciente(nombre, peso, altura)
                pacientes.append(paciente)
            case "b":
                for paciente in pacientes:
                    if paciente.imc() < 18.5:
                        print(paciente.nombre)
            case "c":
                try:
                    sumaPesos = 0
                    for paciente in pacientes:
                        sumaPesos += paciente.peso
                    nroPacientes = len(pacientes)
                    promedio = sumaPesos / nroPacientes
                    print(promedio)
                except ZeroDivisionError:
                    pass


if __name__ == "__main__":
    main()