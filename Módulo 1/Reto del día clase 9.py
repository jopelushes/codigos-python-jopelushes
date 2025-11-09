# Reto del día clase 9
# Autor: Jonathan Perulles Cárdenas
# Fecha: 23 de octubre de 2025

# Se crea la tupla de tipos de registros válidos
TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")

# Función para registrar una línea de texto
def registrar():
    try:
        while True:
            entrada = input(f"Ingresa el tipo de entrada ({', '.join(TIPOS_ENTRADA_VALIDOS)}): ").strip()
            if entrada.capitalize() in TIPOS_ENTRADA_VALIDOS:
                descripcion = input("Ingresa la descripción del tipo de entrada: ").strip()
                with open("laboratorio.txt", "a") as archivo:
                    archivo.write(f"TIPO: {entrada.capitalize()}, DESCRIPCIÓN: {descripcion}\n")
                print("Entrada registrada exitosamente :)")
                break
            else:
                print("Tipo de entrada no válido, intenta de nuevo")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    except FileNotFoundError:
        print("El archivo no se encontró, creando uno nuevo...")
        with open("laboratorio.txt", "w") as archivo:
            archivo.write("")
        print("Archivo creado exitosamente, intenta registrar de nuevo.")

# Función para ver el log de textos registrados
def ver_log():
    try:
        with open("laboratorio.txt", "r") as archivo:
            contenido = archivo.readlines()
            if len(contenido) == 0:
                print("El registro está vacío :(")
            else:
                print("Contenido del registro:")
                for linea in contenido:
                    print(linea.strip())
    except FileNotFoundError:
        print("El archivo no se encontró, no hay registros para mostrar :(")
        with open("laboratorio.txt", "w") as archivo:
            archivo.write("")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para salir del sistema
def salir():
    print("Adiós, saliste del editor de textos :)")

# Bucle principal
while True:
    try:
        opcion = input("Bienvenido, ingresa la operación: registrar, ver_log o salir: ").strip().lower()
        if opcion == "registrar":
            registrar()
        elif opcion == "ver_log":
            ver_log()
        elif opcion == "salir":
            salir()
            break
        else:
            print("Opción no válida, intenta de nuevo")
    except TypeError:
        print("Opción no válida, intenta de nuevo")
    except Exception as e:
        print(f"Ocurrió un error: {e}")