from datetime import datetime

archivoLog = f"log/{datetime.now().strftime("%d-%m-%Y")}-airEuropa.log"
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
info ="INFO"
error = "ERROR"
msjMenu = "MENU PRINCIPAL"
msjConsulta1 = "CONSULTAR VUELOS POR CLIENTE"
msjConsulta2 = "CONSULTAR DIRECCION POR CLIENTE"
msjConsulta3 = "CONSULTAR CLIENTES POR VUELO"
msjUpdate = "ACTUALIZAR MUERTOS"
msjPermisos = "EL USUARIO INTRODUCIDO"
errDato = "TIPO DE DATO INTRODUCIDO INCORRECTO"
errUserNull = "NO EXISTE"
errUserPermisos = "NO TIENE PERMISOS PARA REALIZAR ESTA OPERACION"

def escribirError(mensaje, motivo):
    with open(archivoLog, "a") as f:
        f.write(f"{fecha} {error} {mensaje} {motivo}\n")
def escribirInfo(mensaje):
    with open(archivoLog, "a") as f:
        f.write(f"{fecha} {info} {mensaje}\n")
