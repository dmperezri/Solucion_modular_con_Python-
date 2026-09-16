import os
from utilerias import limpiar_pantalla, leer_numero

def main():
    mensaje = "Bienvenido al sistema de facturación"
    impuesto = 0.15
    nombre = None
    precio = 0.00
    cantidad = 0
    porcentaje = 0.00
    impuesto = 0.15
    total = subtotal = descuento = 0.00

    # Leer nombre del cliente
    nombre = leer_cliente(mensaje)

    # Leer precio, cantidad y porcentaje de descuento
    precio = leer_numero("Ingrese el precio del producto: ")
    cantidad = leer_numero("Ingrese la cantidad del producto: ", tipo=int)
    porcentaje = leer_numero("Ingrese el porcentaje de descuento: ")

    # Calcular factura
    total, subtotal, descuento, iva = calcular_total(precio,cantidad,porcentaje,impuesto)

    # Mostrar factura
    mostrar_factura(nombre,precio,cantidad,porcentaje,subtotal,descuento,iva,total)



def leer_cliente(mensaje):
    limpiar_pantalla()

    print(mensaje)
    print("*" * 30)

    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if not nombre.strip():
            print("El nombre del cliente no puede estar vacío. Por favor, ingrese un nombre válido.")
        else:
            break

    return nombre


def calcular_total(precio, cantidad, porcentaje, impuesto):

    # Calcular subtotal
    subtotal = calcular_subtotal(precio, cantidad)

    # Calcular descuento
    descuento = calcular_descuento(subtotal, porcentaje)

    # Calcular IVA
    iva = calcular_IVA(subtotal, impuesto)

    # Calcular total
    total = subtotal - descuento + iva

    return total, subtotal, descuento, iva


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad

    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * (porcentaje / 100)

    return descuento


def calcular_IVA(subtotal, impuesto):
    iva = subtotal * impuesto

    return iva


def mostrar_factura(nombre,precio,cantidad,porcentaje,subtotal,descuento,iva,total):
    limpiar_pantalla()

    print("=" * 35)
    print("             FACTURA")
    print("=" * 35)

    print("Cliente:", nombre)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Descuento:", porcentaje, "%")

    print("-" * 35)

    print("Subtotal:", subtotal)
    print(f"Descuento: {descuento:.1f}")
    print(f"IVA (15%): {iva:.1f}")

    print("-" * 35)

    print(f"Total: {total:.1f}")

    print("=" * 35)


def calcular_total_productos()

main()