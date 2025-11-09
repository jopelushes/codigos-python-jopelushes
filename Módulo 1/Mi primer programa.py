# Comentario de una línea con #

# Para comentar varias líneas se usa """"

"""
Este es un bloque de comentario
que puede ocupar varias líneas
"""

print("Hola mundo! :)")

"""
Las variables en Python no necesitan declaración previa
y pueden cambiar de tipo dinámicamente
"""

numero = 5                                          # Variable entera
numero_decimal = 3.14                               # Variable decimal
cadena = "Jonathan"                                 # Variable cadena
booleano = True                                     # Variable booleana
lista = [1, 2, 3, 4, 5]                             # Variable lista (array list)
tupla = (1, 2, 3)                                   # Variable tupla (array inmutable)
conjunto = {1, 2, 3}                                # Variable conjunto (set)
diccionario = {"nombre": "Jonathan", "edad": 30}    # Variable diccionario (key-value pairs)

# Para saber qué tipo de dato es una variable se usa type()
print("Imprimiendo el tipo de dato de las variables:")
print(type(numero))          # <class 'int'>
print(type(numero_decimal))  # <class 'float'>

# Imprimir los datos en consola
print("Imprimiendo el tipo de dato de las variables:")
print(numero)          # <class 'int'>
print(numero_decimal)  # <class 'float'>
