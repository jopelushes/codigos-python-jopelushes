# Reto del día 
# Autor: Jonathan Perulles Cárdenas
# Fecha: 16 de octubre de 2025

lista_compras = ["pan", "leche", "huevos", "jabón", "arroz"]

opcion = int(input("¿Qué quieres hacer? 1. Añadir un artículo, 2. Eliminar un artículo, 3. Ver la lista de compras: "))
if opcion == 1:
    articulo = input("Que quieres añadir a la lista de compras?: ")
    lista_compras.append(articulo)
    print(f"Has añadido {articulo} a tu lista. Tu lista ahora es: {lista_compras}")
elif opcion == 2:
    articulo = input("Que quieres eliminar a la lista de compras?: ")
    if articulo not in lista_compras:
        print(f"{articulo} no está en la lista de compras.")
    else: 
        lista_compras.remove(articulo)
        print(f"Has quitado {articulo} de tu lista. Tu lista ahora es: {lista_compras}")
elif opcion == 3:
    print(f"Necesitas comprar estas cosas para la despensa: {lista_compras}")
else:
    print("Opción inválida! :(")

print("Tu lista ha sido actualizada, bye!")