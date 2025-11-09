# Reto del día clase 2
# Autor: Jonathan Perulles Cárdenas
# Fecha: 14/10/2025

# Primera calculadora de operaciones básicas
print("Bienvenido a la calculadora de operaciones básicas")
a = float(input("Teclea el primer número: "))
b = float(input("Teclea el segundo número: "))

print(f"El resultado de sumar {a} + {b} es: {a + b}")
print(f"El resultado de restar {a} - {b} es: {a - b}")
print(f"El resultado de multiplicar {a} * {b} es: {a * b}")
print(f"El resultado de dividir {a} / {b} es: {a / b}")
print(f"El resultado del módulo 2 de {a} es: {a % 2}")
print(f"El resultado del módulo 2 de {b} es: {b % 2}")
print(f"El resultado de la potencia cúbica de {a} es: {a ** 3}")
print(f"El resultado de la potencia cúbica de {b} es: {b ** 3}")

# Segunda calculadora de operaciones lógicas
print("Bienvenido a la calculadora de operaciones lógicas")
x = int(input("Teclea el primer número: "))
y = int(input("Teclea el segundo número: "))

# Asignación suma 2
x += 2
y += 2
print(f"La asignación suma 2 de ambos números es {x} y {y} ")

# Devolución a valor original y asignación resta 13
x -= 2
y -= 2
x -= 13
y -= 13
print(f"La asignación resta 13 de ambos números es {x} y {y} ")

# Devolución a valor original y operadores lógicos
x += 13 
y += 13
print(f"Igualdad: {x == y}")
print(f"Desigualdad: {x != y}")
print(f"Mayor que: {x > y}")
print(f"Menor que: {x < y}")
