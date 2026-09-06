class Foco:
    def __init__(self):
        self.estado = False
    def encender(self):
        if self.estado == False:
            self.estado = True
        else:
            print("El foco ya esta encendido")
    def apagar(self):
        if self.estado == True:
            self.estado = False
        else:
            print("El foco ya esta apagado")
    def estadoFoco(self):
        if self.estado:
            print("Encendido")
        else:
            print("Apagado")

f1 = Foco()
f1.estadoFoco()
f1.encender()
f1.estadoFoco()
f1.encender()