from utilerias import limpiar_pantalla, leer_numero


def main():
    mensaje = "Bienvenido al sistema de facturación"

    impuesto = 0.15
    limite = 10
    porcentaje = 0.00

    nombre = leer_cliente(mensaje)

    # CAMBIO #1
    # Ingreso del producto 1
    print("\nProducto #1")
    nombre1 = input("Ingrese el nombre del producto: ")
    precio1 = leer_numero("Ingrese el precio del producto: ",tipo=float)
    cantidad1 = leer_numero("Ingrese la cantidad del producto: ",tipo=int)

    # Ingreso del producto 2
    print("\nProducto #2")
    nombre2 = input("Ingrese el nombre del producto: ")
    precio2 = leer_numero("Ingrese el precio del producto: ",tipo=float)
    cantidad2 = leer_numero("Ingrese la cantidad del producto: ",tipo=int)

    porcentaje = leer_numero("\nIngrese el porcentaje de descuento: ",tipo=float)

    (total,total_productos,cantidad_total,subtotal1,subtotal2,descuento,tipo_descuento,iva) = calcular_total( precio1, precio2, cantidad1, cantidad2, porcentaje,impuesto,limite)

    mostrar_factura(nombre,nombre1,nombre2,precio1,precio2,cantidad1,cantidad2,subtotal1,subtotal2,porcentaje,total_productos,descuento,tipo_descuento,iva,total)


def leer_cliente(mensaje):
    limpiar_pantalla()

    print(mensaje)
    print("*" * 30)

    while True:
        nombre = input("Ingrese el nombre del cliente: ")

        if not nombre.strip():
            print("El nombre del cliente no puede estar vacío.\n""Por favor, ingrese un nombre válido.")
        else:
            break

    return nombre


def calcular_total(precio1,precio2,cantidad1,cantidad2,porcentaje,impuesto,limite):
    # CAMBIO #1
    (total_productos,cantidad_total,subtotal1,subtotal2) = calcular_total_productos(precio1,precio2,cantidad1,cantidad2)

    descuento, tipo_descuento = calcular_descuento(total_productos,porcentaje,cantidad_total,limite)

    iva = calcular_iva(total_productos,impuesto)

    total = total_productos - descuento + iva

    return (total,total_productos,cantidad_total,subtotal1,subtotal2,descuento,tipo_descuento,iva)


# CAMBIO #1
def calcular_total_productos(precio1,precio2,cantidad1,cantidad2):
    subtotal1 = calcular_subtotal1(precio1,cantidad1)
    subtotal2 = calcular_subtotal2( precio2, cantidad2)

    total_productos = subtotal1 + subtotal2
    cantidad_total = cantidad1 + cantidad2

    return (total_productos,cantidad_total,subtotal1,subtotal2)


def calcular_subtotal1(precio1, cantidad1):
    subtotal1 = precio1 * cantidad1
    return subtotal1


def calcular_subtotal2(precio2, cantidad2):
    subtotal2 = precio2 * cantidad2
    return subtotal2


def calcular_descuento(total_productos, porcentaje,cantidad_total,limite
):
    # CAMBIO #2
    # Primero se verifica el descuento por volumen
    descuento_volumen = calcular_descuento_por_volumen(total_productos,cantidad_total,limite)

    # Solo se aplica un tipo de descuento
    if descuento_volumen > 0:
        descuento = descuento_volumen
        tipo_descuento = "Descuento por volumen (5%)"
    else:
        descuento = total_productos * (porcentaje / 100)
        tipo_descuento = f"Descuento ({porcentaje}%)"

    return descuento, tipo_descuento


# CAMBIO #2
def calcular_descuento_por_volumen(
    total_productos,
    cantidad_total,
    limite
):
    porcentaje_volumen = 0.05

    if cantidad_total > limite:
        descuento_volumen = total_productos * porcentaje_volumen
    else:
        descuento_volumen = 0.00

    return descuento_volumen


def calcular_iva(total_productos, impuesto):
    iva = total_productos * impuesto

    return iva


def mostrar_factura(nombre,nombre1,nombre2,precio1,precio2,cantidad1,cantidad2,subtotal1,subtotal2,porcentaje,total_productos,descuento,tipo_descuento,iva,total):
    limpiar_pantalla()

    print("=" * 40)
    print("               FACTURA")
    print("=" * 40)

    print("Cliente:", nombre)

    print("\nPRODUCTO #1")
    print("-" * 40)
    print("Nombre:", nombre1)
    print(f"Precio: {precio1:.2f}")
    print("Cantidad:", cantidad1)
    print(f"Subtotal: {subtotal1:.2f}")

    print("\nPRODUCTO #2")
    print("-" * 40)
    print("Nombre:", nombre2)
    print(f"Precio: {precio2:.2f}")
    print("Cantidad:", cantidad2)
    print(f"Subtotal: {subtotal2:.2f}")

    print("-" * 40)

    print(f"Total productos: {total_productos:.2f}")
    print(f"{tipo_descuento}: {descuento:.2f}")
    print(f"IVA (15%): {iva:.2f}")

    print("-" * 40)
    print(f"Total: {total:.2f}")
    print("=" * 40)


main()