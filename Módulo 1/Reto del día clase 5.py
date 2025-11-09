# Reto del día clase 5
# Autor: Jonathan Perulles Cárdenas
# Fecha: 17 de octubre de 2025

# Sistema que pide calificacione y los clasifica
numero_alumnos = int(input("Ingresa el número de alumnos del grupo: "))
# Definir listas vacias para clasificar a los alumnos
reprobados = []
aprobados = []
excelentes = []
# Inicializar variables para el promedio y calificaciones extrema
calificacion_grupal = 0.0

for i in range(numero_alumnos):
    nombre_alumno = input(f"Ingresa el nombre del alumno {i + 1}: ")
    calificacion = float(input(f"Ingresa la calificación de {nombre_alumno}: "))
    # Clasifica los alumnos en listas de acuerdo a su calificación
    if calificacion < 5:
        reprobados.append(nombre_alumno)
    elif calificacion < 10:
        aprobados.append(nombre_alumno)
    elif calificacion == 10:
        excelentes.append(nombre_alumno)
    # Obtiene el promedio grupal
    calificacion_grupal += calificacion
    # Determina la calificación más alta y más baja
    if i == 0:
        calificacion_mas_alta = calificacion
        calificacion_mas_baja = calificacion
    else:
        if calificacion > calificacion_mas_alta:
            calificacion_mas_alta = calificacion
        if calificacion < calificacion_mas_baja:
            calificacion_mas_baja = calificacion

promedio_grupal = calificacion_grupal / numero_alumnos
# Imprimir los resultados
print(f"Hola profesor, tienes {numero_alumnos} alumnos en el grupo.")
print(f"El promedio grupal es: {promedio_grupal}")
print(f"La calificación más alta es {calificacion_mas_alta} y la más baja es {calificacion_mas_baja}.")
print(f"Los alumnos reprobados son: {reprobados}")
print(f"Los alumnos aprobados son: {aprobados}")
print(f"Los alumnos con calificación excelente son: {excelentes}")