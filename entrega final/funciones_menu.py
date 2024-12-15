from funciones_database import *


# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************


# Funcion que muestra el menú
def menu_mostrar_opciones():

    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    # Agregan un modulo de validacion para evitar errores - PENDIENTE

    # Ingreso y validacion de opcion
    while True:
        # Codigo a testear
        opcion = input("Ingrese la opción deseada: ").strip()
        # Lo que hace cuando no se ingresa dato
        if not opcion:
            print("No se admite dato nulo. Ingrese la opcion: ")
        else:
            break

    # retorno un Str
    return opcion


"""
menu_registrar_producto()

1. solicita al usuario el ingreso de los datos
2. *** valida los valores y tipos de datos ingresados
3. almacena los valores en un diccionario llamado producto
4. llama a db_insertar_producto(producto) y le pasa como argumento el diccionario producto para que lo inserte en la base de datos
"""


def menu_registrar_producto():
    print("\n***REGRISTRO DE PRODUCTO***\n")
    print("Ingrese los siguientes datos del producto:")
    # TO DO: VALIDAR VALORES Y TIPOS DE DATOS

    # Ingreso y validacion del nombre
    while True:
        # Codigo a testear
        nombre = input("Nombre: ").strip()
        # Lo que hace cuando no se ingresa dato
        if not nombre:
            print("No se admite dato nulo. Ingrese el nombre: ")
        else:
            break

    # Ingreso y validacion de la descripcion admite dato nulo
    while True:
        descripcion = input("Descripción: ").strip()
        break

    # Ingreso y validacion de la categoria
    while True:
        # Codigo a testear
        categoria = input("Categoría: ").strip()
        # Lo que hace cuando no se ingresa dato
        if not categoria:
            print("No se admite dato nulo. Ingrese la categoria: ")
        else:
            break

    # Ingreso y validacion de la cantidad
    while True:
        try:
            # Codigo a testear
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero")

    # Ingreso y validacion del precio
    while True:
        try:
            # Codigo a testear
            precio = float(input("Precio: "))
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero o decimal")

    resultado = db_insertar_producto(nombre, descripcion, categoria, cantidad, precio)
    if resultado == True:
        print("Registro insertado exitosamente!")
    else:
        print("Algo fallo")


"""
menu_mostrar_productos()

1. no recibe ningún argumento
2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
3. si hay productos, los muestra en consola usando un bucle for
4. si no hay productos, muestra un mensaje indicando que no hay productos
"""


def menu_mostrar_productos():
    lista_productos = db_get_productos()  # retorna una lista

    print("\n***MOSTRAR PRODUCTOS***\n")

    if not lista_productos:  # si no hay productos
        print("No hay productos que mostrar")
    else:  # si hay productos mostrarlos todos
        for producto in lista_productos:
            print(
                f"ID: {producto[0]},Producto: {producto[1]}, Descripcion: {producto[2]}, Categoria: {producto[3]}, Cantidad: {producto[4]}, Precio: {producto[5]}"
            )


""""
def menu_actualizar_producto()

1. solicita al usuario que ingrese el id del producto a modificar
2. busca el producto en la tabla (si no existe informamos)
3. muestra la cantidad actual y solicita que ingrese la nueva cantidad
4. llama a db_actualizar_registro(id, nueva_cantidad) para que actualice la cantidad

"""


def menu_actualizar_producto():
    print("\n***ACTUALIZAR UN PRODUCTO***\n")
    # Validacion de la id
    while True:
        try:
            # Codigo a testear
            id = int(input("Ingrese el id del producto a actualizar: "))
            producto = db_get_producto_by_id(id)
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero")

    if producto:
        print(
            f"ID: {producto[0]}, Producto: {producto[1]}, Descripcion: {producto[2]}, Categoria: {producto[3]}, Cantidad: {producto[4]}, Precio: {producto[5]}"
        )
        while True:
            # Ingresar y validar la cantidad nueva
            try:
                # Codigo a testear
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                db_actualizar_producto(id, nueva_cantidad)
                print("El producto ha sido actualizado con exito")
                break
            except ValueError:
                # Lo que hace cuando encuentra exception
                print(f"Error: debe ingresar un número entero")

    else:
        print("No existe un producto con ese id")


"""
menu_eliminar_producto()

1. solicita al usuario que ingrese el id del producto a eliminar
2. busca el producto por el id en la tabla (si no existe informa)
3. muestra el producto y solicita confirmación
4. llama a db_eliminar_producto(id) para eliminar el registro con el id indicado
"""


def menu_eliminar_producto():
    print("\n***ELIMINAR UN PRODUCTO***\n")

    while True:
        # Validar el id
        try:
            # Codigo a testear
            id = int(input("Ingrese el id del producto a eliminar: "))
            producto = db_get_producto_by_id(id)
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero")

    if producto:  # mostrar el producto que se eliminara
        print(producto)
        db_eliminar_producto(id)
        print("Producto eliminado exitosamente!")
    else:
        print("No existe el producto con el id ingresado")


"""
menu_buscar_producto()
1. solicita al usuario que ingrese el id del producto a buscar
2. llama a db_get_producto_by_id(id)
3. si el producto existe lo muestra en consola, de lo contrario informa el error
"""


def menu_buscar_producto():
    print("\n***BUSCAR UN PRODUCTO***\n")
    while True:
        # Validar el id
        try:
            # Codigo a testear
            id = int(input("Ingrese el id a buscar: "))
            producto = db_get_producto_by_id(id)
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero")

    if not producto:
        print("No se ha encontrado el producto")
    else:  # mostrar el producto encontrado
        print(
            f"ID: {producto[0]}, Producto: {producto[1]}, Descripcion: {producto[2]}, Categoria: {producto[3]}, Cantidad: {producto[4]}, Precio: {producto[5]}"
        )


"""
menu_reporte_bajo_stock()
1. solicita al usuario que ingrese la cantidad mínima de stock 
2. llama a db_get_productos_by_condicion(condicion) que retorna una lista_productos
3. si hay productos, los muestra en consola, de lo contrario informa
"""


# Generar el reporte
def menu_reporte_bajo_stock():
    print("\n***REPORTE DE BAJO STOCK***\n")
    # Validar el umbral minimo de stock
    while True:
        # Codigo a testear
        try:
            minimo_stock = int(input("ingrese el minimo de stock: "))
            break
        except ValueError:
            # Lo que hace cuando encuentra exception
            print(f"Error: debe ingresar un número entero")

    lista_productos = db_get_productos_by_condicion(minimo_stock)

    if lista_productos:
        # recorre la lista para mostrar los productos
        for producto in lista_productos:
            print(
                f"ID: {producto[0]}, Producto: {producto[1]}, Cantidad: {producto[4]}"
            )
    else:  # si no cumple la condición, no muestra el producto
        print("No hay productos con stock menor a " + str(minimo_stock))
