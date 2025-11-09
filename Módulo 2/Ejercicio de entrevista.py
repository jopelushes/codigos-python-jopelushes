# Ejercicio de entrevista
# Módulo 2
# Autor: Jonathan Perulles Cárdenas
# Fecha: 27 de octubre de 2025

import string
from unidecode import unidecode

def contar_palabras(archivo_texto, archivo_conteo, palabras_a_contar):
    try:
        with open(archivo_texto, "r") as f:
            texto = f.read()
        
        # Normalizando el texto
        texto = texto.lower()
        texto = unidecode(texto)
        tabla_puntuacion = str.maketrans('', '', string.punctuation)
        texto = texto.translate(tabla_puntuacion)
        texto = texto.strip()

        palabras = texto.split()
        conteo = {}
        for palabra in palabras:
            conteo[palabra] = conteo.get(palabra,0) + 1

        # Guardar las palabras en el archivo
        with open(archivo_conteo, "w") as salida:
            salida.write("Conteo de palabras: \n")
            salida.write("="*30)
            for palabra in palabras_a_contar:
                palabra_normalizada = palabra.lower()
                palabra_normalizada = unidecode(palabra_normalizada)
                palabra_normalizada = palabra_normalizada.translate(tabla_puntuacion)
                palabra_normalizada.strip()
                contador = conteo.get(palabra_normalizada)
                print(f"{palabra}: {contador} veces\n")

        print(f"Conteo exitoso, el archivo '{archivo_conteo}' ha sido creado con éxito")

    except FileNotFoundError:
        print(f"No se encontró el archivo '{archivo_texto}'.")
    except Exception as e:
        print(f"Error: {e}")

palabras_a_contar = ["Dostoievski", "sinónimos", "Horiki", "humanos", "miedo", "palabras"]
contar_palabras("Fragmento_Indigno_de_ser_humano.txt", "conteo_palabras.txt", palabras_a_contar)
