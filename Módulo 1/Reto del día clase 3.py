# Reto del día clase 3
# Autor: Jonathan Perulles Cárdenas
# Fecha: 15 de octubre de 2025

nombre = input("Bienvenido. Ingresa tu nombre: ")
año_nacimiento = int(input("Genial, ahora ingresa tu año de nacimiento: "))
videojuegos = input(f"Super {nombre}, ahora ingresa tus 3 videojuegos favoritos separados por comas: ")
# Se crea la lista del perfil primero con nombre
perfil = [nombre]
# Se añade la edad al final de la lista actual
perfil.append(2025 - año_nacimiento)
# Se crea una lista de videojuegos a partir del string ingresado y extiende la lista perfil
lista_videojuegos = videojuegos.split(", ")
perfil.extend(lista_videojuegos)
# Se añade el estatus de usuario activo al principio de la lista
perfil.insert(0, True)
# Quitar el primer juego de la lista y guardarlo en una variable
juego_favorito = perfil.pop(3)
# Comprobaciones lógicas
es_mayor_de_edad = perfil[2] >= 18
nombre_largo = len(perfil[1]) > 10
es_gamer_retro = "pacman" in perfil
# Mostrar el perfil completo
print(f"Tu perfil es: {perfil}")
print(f"Tu juego favorito es {juego_favorito}, que buenos gustos tienes {nombre}")
print(f"Hola {nombre}, mayoría de edad: {es_mayor_de_edad}, nombre largo: {nombre_largo}, eres gamer retro: {es_gamer_retro}")