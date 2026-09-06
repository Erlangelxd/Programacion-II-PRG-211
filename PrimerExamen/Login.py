class Usuario:
    def __init__(self):
        self.usuario = "Erlanxd"
        self.contraseña = "UPEA123"
        self.activo = False
    def verificaUsuario(self, entrada_contraseña):
        if self.contraseña == entrada_contraseña:
            self.activo = True
        else:
            self.activo = False
    def estado(self):
        if self.activo:
            print("Ingreso exitoso")
        else:
            print("Denegado")


us = Usuario()
contra = input("Dame tu contraseña: ")
us.verificaUsuario(contra)
us.estado()
