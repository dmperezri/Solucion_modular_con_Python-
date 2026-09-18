import os


def limpiar_pantalla():
    os.system('cls')


def leer_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))

            if valor < 0:
                print(
                    "El valor ingresado no puede ser negativo. "
                    "Por favor, ingrese un número válido."
                )
                continue

            return valor

        except ValueError:
            print(
                "Entrada inválida. "
                "Por favor, ingrese un número válido."
            )