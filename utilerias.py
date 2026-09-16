import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def leer_numero(mensaje, tipo=False):
    while True:
        try:
            if tipo:
                valor = float(input(mensaje))
            else:
                valor = int(input(mensaje))

            if valor < 0:
                print("El valor ingresado no puede ser negativo. Por favor, ingrese un número válido.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")