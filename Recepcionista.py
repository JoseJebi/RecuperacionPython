from Empleado import Empleado


class Recepcionista(Empleado):
    def __init__(self, nick, correo, num_consultas):
        super().__init__(nick, correo)
        self.num_consultas = num_consultas
