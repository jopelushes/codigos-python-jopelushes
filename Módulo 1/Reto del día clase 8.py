# Reto del día clase 8
# Autor: Jonathan Perulles Cárdenas
# Fecha: 22 de octubre de 2025

# Se crea el diccionario de la BD y la tupla de partes
base_de_partes = {}
componentes_validos = ("Motor", "Sensor", "Batería", "Chasis", "Rueda")

# Función para registrar un componente
def registrar():
    clave = input("Ingresa la clave del componente: ")
    if clave in base_de_partes:
        print("Clave ya registrada")
    else:
        print(f"Componentes válidos: {componentes_validos}")
        tipo_componente = input("Ingresa el tipo de componente: ")
        if tipo_componente.capitalize() in componentes_validos:
            resultados_pruebas = []
            error = False
            for i in range(3):
                try:
                    resultado = float(input(f"Ingresa el resultado de la prueba {i + 1} (0 a 100): "))
                    if 0 <= resultado <= 100:
                        resultados_pruebas.append(resultado)
                    else:
                        print("Resultado no válido")
                        error = True
                        break
                except ValueError:
                    print("Ingresa un resultado válido")
                    error = True
                    break
            if not error and len(resultados_pruebas) == 3:
                valor = {"tipo_componente": tipo_componente, "resultados_pruebas": resultados_pruebas, "estado": "Pendiente"}
                articulo = {"clave": clave, "datos": valor}
                base_de_partes[clave] = articulo
                print(f"Componente registrado: {articulo}")
            else:
                print("No se registró el componente debido a errores en los resultados")
        else:
            print("Tipo de componente no válido")

# Función para buscar un componente
def buscar():
    clave_buscar = input("Ingresa la clave del componente a buscar: ")
    if clave_buscar in base_de_partes:
        print(f"Componente: {base_de_partes[clave_buscar]['datos']}")
    else:
        print("No se encontró un componente con esa clave")

# Función para evaluar un componente
def evaluar():
    clave_evaluar = input("Ingresa la clave del componente a evaluar: ")
    if clave_evaluar in base_de_partes:
        resultados = base_de_partes[clave_evaluar]["datos"]["resultados_pruebas"]
        promedio = sum(resultados) / len(resultados)
        if promedio >= 90.0:
            estado = "Aprobado"
        else:
            estado = "Rechazado"
        base_de_partes[clave_evaluar]["datos"]["estado"] = estado
        print(f"El componente con clave {clave_evaluar} tuvo una calificación de {promedio} y ha sido evaluado como: {estado}")
    else:
        print("No se encontró un componente con esa clave")

# Función para ver el inventario de componentes
def ver_inventario():
    if len(base_de_partes) == 0:
        print("No hay componentes registrados")
    else:
        for clave, info in base_de_partes.items():
            print(f"Clave: {clave}, Tipo: {info['datos']['tipo_componente']}, Estado: {info['datos']['estado']}")

# Función para contar componentes
def contar_componentes(lista, tipo):
    if not lista:
        return 0
    primer_elemento = lista[0]
    resto = lista[1:]
    if primer_elemento["datos"]["tipo_componente"].capitalize() == tipo.capitalize():
        return 1 + contar_componentes(resto, tipo)
    else:
        return contar_componentes(resto, tipo)

def contar():
    try:
        componente = input("Ingresa el tipo de componente a contar: ")
        if componente.capitalize() not in componentes_validos:
            print("Tipo de componente no válido")
            return
        elif len(base_de_partes) == 0:
            print("No hay componentes registrados")
        else:
            lista_componentes = list(base_de_partes.values())
            contador = contar_componentes(lista_componentes, componente)
            print(f"Total de componentes del tipo {componente}: {contador}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para salir del sistema
def salir():
    print("Cerrando el sistema de CQ...")
    print("Adiós :)")

# Se crea el ciclo del menú de opciones
while True:
    try:
        opcion = input("Bienvenido, ingresa la operación: registrar, buscar, evaluar, ver_inventario, contar o salir: ")
        if opcion == "registrar":
            registrar()
        elif opcion == "buscar":
            buscar()
        elif opcion == "evaluar":   
            evaluar()
        elif opcion == "ver_inventario":
            ver_inventario()
        elif opcion == "salir":
            salir()
            break
        else:
            print("Opción no válida, intenta de nuevo")
    except TypeError:
        print("Opción no válida, intenta de nuevo")


