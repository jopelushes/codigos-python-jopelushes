# Reto del día clase 7
# Autor: Jonathan Perulles Cárdenas
# Fecha: 21 de octubre de 2025

# Se crea el diccionario base, el diccionario del alumno y la tupla de materias
registro_estudiantes = {}
alumno = {"clave": ""}
materias_validas = ("Español", "Matematicas", "Artes")

# Ciclo del menú de opciones
while True:
    try:
        opcion = input("Escribe la opción: registrar, buscar, promedio, ver_todos, cursos_unicos o salir: ").lower()
        if opcion == "registrar":
            clave = input("Ingresa la clave del estudiante: ")
            if clave in registro_estudiantes:
                print("Ya hay un estudiante registrado con esa clave")
            else:
                nombre = input("Ingresa el nombre del estudiante: ")
                print(f"Materias válidas: {materias_validas}")
                validar_materia = input("Ingresa una materia de la lista anterior: ")
                if validar_materia.capitalize() in materias_validas:
                    calificaciones = []
                    error = False
                    for i in range(3):
                        try:
                            calificacion = float(input(f"Ingresa la calificación de {materias_validas[i]}: "))
                            if 0 <= calificacion <= 10:
                                calificaciones.append(calificacion)
                            else:
                                print("Calificación no válida")
                                error = True
                                break
                        except ValueError:
                            print("Ingresa una calificación válida")
                            error = True
                            break
                    if not error and len(calificaciones) == 3:
                        valor = {"nombre": nombre, "calificaciones": calificaciones}
                        alumno = {"clave": clave, "datos": valor}
                        registro_estudiantes[clave] = alumno
                        print(f"Alumno registrado: {alumno}")
                    else: 
                        print("No se registró al estudiante debido a errores en las calificaciones")
                else:
                    print("Materia no válida, no se registró al estudiante")
        elif opcion == "buscar":
            clave_buscar = input("Ingresa la clave del estudiante a buscar: ")
            if clave_buscar in registro_estudiantes:
                print(f"Estudiante encontrado: {registro_estudiantes[clave_buscar]['datos']}")
            else:
                print("No se encontró un estudiante con esa clave")
        elif opcion == "promedio":
            clave_promedio = input("Ingresa la clave del estudiante para obtener su promedio: ")
            if clave_promedio in registro_estudiantes:
                calificaciones = registro_estudiantes[clave_promedio]["datos"]["calificaciones"]
                promedio = sum(calificaciones) / len(calificaciones)
                nom = registro_estudiantes[clave_promedio]["datos"]["nombre"]
                print(f"El promedio del estudiante {nom} es: {promedio:.2f}")
            else:
                print("No se encontró un estudiante con esa clave")
        elif opcion == "ver_todos":
            if len(registro_estudiantes) == 0:
                print("No hay estudiantes registrados")
            else:
                for clave, info in registro_estudiantes.items():
                    print(f"Clave: {clave}, Nombre: {info['datos']['nombre']}")
        elif opcion == "salir":
            print("Has salido del menú de opciones, adiós")
            break
        else:
            print("Opción no válida, intenta de nuevo")
    except TypeError:
        print("Opción no válida, intenta de nuevo")
