# Ejercicio de entrevista 2
# Módulo 2
# Autor: Jonathan Perulles Cárdenas
# Fecha: 30 de octubre de 2025

# Se genera una lista de números
lista = [1, 8 , 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3]

def num_no_repetidos(lista):
    lista_original = set()
    lista_no_repetidos = []
    for i in lista:
        if i not in lista_original:
            lista_no_repetidos.append(i)
            lista_original.add(i)
    return lista_no_repetidos

lista_nueva = num_no_repetidos(lista)
print(f"Lista de números original: {lista}")
print(f"Lista de números no repetidos: {num_no_repetidos(lista)}")
