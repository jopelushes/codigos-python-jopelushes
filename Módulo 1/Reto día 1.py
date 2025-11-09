# Reto del día clase 1
# Autor: Jonathan Perulles Cárdenas

# Pedir al usuario datos y primero imprime dato por dato y al final un mensaje con todos los datos

nombre = input("¿Cómo te llamas?")
print(f"Bienvenido {nombre} :D")

edad = int(input("¿Cuántos años tienes?"))
print(f"Wow! Tienes {edad} años!")

frase = input("Escribe tu frase favorita: ")
print(f"Tu frase favorita es: {frase}")

dinero_disponible = float(input("¿Cuánto dinero tienes disponible?"))
print(f"Solo tienes {dinero_disponible} pesos en tu cuenta :O")

# Mostar mensaje total
print(f"Hola de nuevo {nombre}, tienes {edad} años y tu frase favorita es {frase}. Solo tienes {dinero_disponible} pesos disponibles en tu cuenta, que mal! :(")