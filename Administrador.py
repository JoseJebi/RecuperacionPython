from Empleado import Empleado


class Administrador(Empleado):
    def __init__(self, nick, correo, num_actualizaciones):
        super().__init__(nick, correo)
        self.num_actualizaciones = num_actualizaciones

