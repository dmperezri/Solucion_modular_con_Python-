from utilerias import limpiar_pantalla, leer_numero


def main():
    mensaje = "Bienvenido al sistema de facturación"

    impuesto = 0.15
    limite = 10
    nombre = None
    porcentaje = 0.00

    nombre = leer_cliente(mensaje)

    # CAMBIO #1
    # Permitir ingresar varios productos
    cantidad_productos = leer_numero("Ingrese la cantidad de productos diferentes: ",tipo=int) 

    productos = []

    for i in range(cantidad_productos):
        print(f"\nProducto #{i + 1}")
        precio = leer_numero("Ingrese el precio del producto: ",tipo=float)
        cantidad = leer_numero("Ingrese la cantidad del producto: ", tipo=int)
        productos.append((precio, cantidad))

    porcentaje = leer_numero("\nIngrese el porcentaje de descuento: ",tipo=float)

    (total, total_productos, descuento,descuento_volumen,iva) = calcular_total(productos,porcentaje,impuesto,limite)

    mostrar_factura(nombre,productos,porcentaje,total_productos,descuento,descuento_volumen,iva,total)


def leer_cliente(mensaje):
    limpiar_pantalla()

    print(mensaje)
    print("*" * 30)

    while True:
        nombre = input("Ingrese el nombre del cliente: ")

        if not nombre.strip():
            print("El nombre del cliente no puede estar vacío.")
            print("Por favor, ingrese un nombre válido.")

        else:
            break
    return nombre


def calcular_total(productos,porcentaje,impuesto,limite):
    # CAMBIO #1
    # Obtener el total acumulado de todos los productos
    total_productos, cantidad_total = calcular_total_productos(productos)

    # Calcular descuento normal
    descuento = calcular_descuento( total_productos, porcentaje)

    # CAMBIO #2
    # Calcular descuento adicional por volumen
    descuento_volumen = calcular_descuento_por_volumen(total_productos, cantidad_total, limite)

    # Calcular IVA
    iva = calcular_IVA(total_productos,impuesto)

    # Calcular total final
    total = (total_productos - descuento - descuento_volumen + iva)

    return (total,total_productos,descuento,descuento_volumen,iva)


# CAMBIO #1
def calcular_total_productos(productos):
    total_productos = 0.00
    cantidad_total = 0

    for precio, cantidad in productos:
        subtotal = calcular_subtotal(precio,cantidad)

        total_productos += subtotal
        cantidad_total += cantidad
    return total_productos, cantidad_total


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(total_productos, porcentaje):
    descuento = total_productos * (porcentaje / 100)
    return descuento

# CAMBIO #2
def calcular_descuento_por_volumen(total_productos, cantidad_total,limite):
    porcentaje_volumen = 0.05

    if cantidad_total > limite:
        descuento_volumen = (total_productos * porcentaje_volumen)
    else:
        descuento_volumen = 0.00
    return descuento_volumen


def calcular_IVA(total_productos,impuesto):
    iva = total_productos * impuesto
    return iva


def mostrar_factura(nombre, productos,porcentaje, total_productos, descuento, descuento_volumen, iva, total):
    limpiar_pantalla()

    print("=" * 40)
    print("               FACTURA")
    print("=" * 40)
    print("Cliente:", nombre)
    print("\nPRODUCTOS")
    print("-" * 40)

    for i, producto in enumerate(productos):
        precio, cantidad = producto
        subtotal = calcular_subtotal(precio , cantidad )

        print(f"Producto #{i + 1}")
        print(f"Precio: {precio:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Subtotal: {subtotal:.2f}")
        print("-" * 40)

    print(f"Total productos: "f"{total_productos:.2f}")
    print(f"Descuento ({porcentaje}%): "f"{descuento:.2f}")
    print(f"Descuento por volumen: "f"{descuento_volumen:.2f}")
    print(f"IVA (15%): "f"{iva:.2f}")
    print("-" * 40)
    print(f"Total: "f"{total:.2f}")
    print("=" * 40)

    main()