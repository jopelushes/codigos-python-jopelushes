# Reto del día clase 6
# Autor: Jonathan Perulles Cárdenas
# Fecha: 20 de octubre de 2025

inventario = ["pan", "leche", "huevos", "queso", "jamón"]
while True:
    try:
        opcion = input("Bienvenido, escribe la opción: añadir, quitar, ver, inspeccionar o salir: ").lower()
        if opcion == "añadir":
            nuevo_articulo = input("Teclea el artículo a añadir: ")
            inventario.append(nuevo_articulo)
            print(f"{nuevo_articulo} ha sido añadido a la lista :)")
            print(f"Tu inventario actual es: {inventario}")
        elif opcion == "quitar":
            articulo_a_quitar = input("Teclea el artículo a quitar: ")
            if articulo_a_quitar in inventario:
                inventario.remove(articulo_a_quitar)
                print(f"{articulo_a_quitar} ha sido quitado de la lista :)")
                print(f"Tu inventario actual es: {inventario}")
            else:
                print(f"{articulo_a_quitar} no se encuentra en la lista :(")
        elif opcion == "ver":
            if len(inventario) == 0:
                print("La lista esta vacía D:")
            else:
                print(f"Tu inventario actual es: {sorted(inventario)}")
        elif opcion == "inspeccionar":
            try:
                item = int(input(f"¿Qué número de artículo deseas inspeccionar? (1 a {len(inventario)}): "))
                if item >= 1 and item <= len(inventario):
                    print(f"El artículo {item} es: {inventario[item - 1]}")
                    print(f"Tu inventario actual es: {inventario}")
                else:
                    print("Número de item no válido :(")
            except ValueError:
                print("Tienes que ingresar un número entero válido")
        elif opcion == "salir":
            break
        else:
            print("Opción no válida, intenta de nuevo")
    except TypeError:
        print("Opción no válida, intenta de nuevo")
print("Has salido del menú de opciones")
