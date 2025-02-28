from Administrador import Administrador
from Constantes import QUERY_CLIENTES_ACTIVOS, QUERY_VUELOS_BY_PASAJERO, QUERY_VUELOS, UPDATE_MAYORES, UPDATE_MENORES
from Empleados import Empleados
from Log import escribirError, msjMenu, errDato, escribirInfo, msjConsulta1, msjPermisos, errUserNull, errUserPermisos, \
    msjConsulta2
from Recepcionista import Recepcionista
import pandas as pd
from db import PostgreSQLConnection

def usuarios_activos():
    result, column_names = db_connection.execute_query(QUERY_CLIENTES_ACTIVOS)
    if result:
        df = pd.DataFrame(result, columns=column_names)
        print(df)

def mostrar_vuelos():
    usuarios_activos()
    while True:
        try:
            id = int(input("Introduce el id del pasajero: "))
            break
        except ValueError:
            escribirError(msjConsulta1, errDato)
            print("Introduce un numero entero")
    result, column_names = db_connection.execute_query(QUERY_VUELOS_BY_PASAJERO, {'id_pasajero': id})
    if result:
        df = pd.DataFrame(result, columns=column_names)
        print(df)

def comprobar_usuario(empleados):
    nick = input("Introduce el usuario: ")
    for emp in empleados:
        if emp.nick == nick:
            return emp
    print(f"No existe ningun usuario con el nombre {nick}")
    return None

def todos_vuelos():
    result, column_names = db_connection.execute_query(QUERY_VUELOS)
    if result:
        df = pd.DataFrame(result, columns=column_names)
        print(df)

def menu_opcion2(df):
    while True:
        print("\n--- MENÚ ---")
        print("1. Usuario que más ha pagado")
        print("2. Usuario que menos ha pagado")
        print("3. Media del precio de los billetes")
        print("4. Salir")
        while True:
            try:
                opcion = int(input("Opcion elegida: "))
                break
            except ValueError:
                escribirError(msjConsulta2, "TIPO DE DATO INTRODUCIDO INCORRECTO")
                print("Opcion no valida")
        if opcion == 1:
            print(df[df['Precio_billete']==df.Precio_billete.max()])
        elif opcion == 2:
            print(df[df['Precio_billete']==df.Precio_billete.min()])
        elif opcion == 3:
            print(f"Media de precios del billete: {df.Precio_billete.mean()}")
        elif opcion == 4: break
        else:
            print("Opcion no valida")

def mostrar_datos_vuelo():
    todos_vuelos()
    while True:
        try:
            id = int(input("Introduce el id del vuelo: "))
            break
        except ValueError:
            escribirError(msjConsulta2, errDato)
            print("Introduce un numero entero")
    result, column_names = db_connection.execute_query(QUERY_VUELOS_BY_PASAJERO, {'id_vuelo': id})
    if result:
        df = pd.DataFrame(result, columns=column_names)
        print(df)
        menu_opcion2(df)

def asignar_mayor_menor():
    db_connection.execute_query(UPDATE_MAYORES)
    db_connection.execute_query(UPDATE_MENORES)
    print("Usuarios modificados")


def menu():
    empleados = Empleados()
    #añadir aqui a los empleados el admin y el recepcionista
    #cada vez que se realice una actualización o una consulta se deberá sumar 1.
    empleados.empleados.append(Administrador("Admin", "admin@admin.com", 0))
    empleados.empleados.append(Recepcionista("Recepcionista", "recep@gmail.com", 0))

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar los vuelos de un cliente")
        print("2. Mostrar todos los datos de un vuelo")
        print("3. Mayores de edad")

        while True:
            try:
                opcion = int(input("Opcion elegida: "))
                break
            except ValueError:
                escribirError(msjMenu, errDato)
                print("Opcion no valida")
        if opcion == 1:
            user = comprobar_usuario(empleados.empleados)
            if user != None:
                if isinstance(user, Administrador):
                    asignar_mayor_menor()
                    user.num_actualizaciones += 1
                    escribirInfo(msjConsulta1)
                else:
                    escribirError(msjPermisos, errUserNull)
                    print("Usuario invalido")
            else:
                escribirError(msjPermisos, errUserPermisos)
                print("El usuario no existe")

        elif opcion == 2:
            user = comprobar_usuario(empleados.empleados)
            if user != None:
                if isinstance(user, Recepcionista):
                    mostrar_datos_vuelo()
                    user.num_consultas += 1
                    escribirInfo(msjConsulta2)
                else:
                    escribirError(msjPermisos, errUserNull)
                    print("Usuario invalido")
            else:
                escribirError(msjPermisos, errUserPermisos)
                print("El usuario no existe")

        elif opcion == 3:
            user = comprobar_usuario(empleados.empleados)
            if user != None:
                if isinstance(user, Recepcionista):
                    mostrar_datos_vuelo()
                    user.num_consultas += 1
                    escribirInfo(msjConsulta2)
                else:
                    escribirError(msjPermisos, errUserNull)
                    print("Usuario invalido")
            else:
                escribirError(msjPermisos, errUserPermisos)
                print("El usuario no existe")

if __name__ == "__main__":
    db_connection = PostgreSQLConnection()
    db_connection.connect()

    menu()

    db_connection.disconnect()