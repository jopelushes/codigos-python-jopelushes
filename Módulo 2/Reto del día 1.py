# Reto del día clase 1
# Módulo 2
# Autor: Jonathan Perulles Cárdenas
# Fecha: 27 de octubre de 2025

class Componente:
    def __init__(self, numero_serie, tipo_componente, costo):
        self.numero_serie = numero_serie
        self.tipo_componente = tipo_componente
        self.costo = costo

        # Definiendo atributos adicionales
        self.historial_revisiones = []
        self.esta_activo = True
        pass

# Creando los objetos de la clase Componente
c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

# Añadiendo fecha a c1 y cambiar atributo esta_activo de c2
c1.historial_revisiones.append("2025-10-27")
c2.esta_activo = False

# Imprimiendo los atributos de los objetos
print("Serie Componente 1: {c1.numero_serie}, Tipo: {c1.tipo_componente}, Costo: {c1.costo}, Historial de Revisiones: {c1.historial_revisiones}, Está Activo: {c1.esta_activo}".format(c1=c1))
print("Serie Componente 2: {c2.numero_serie}, Tipo: {c2.tipo_componente}, Costo: {c2.costo}, Historial de Revisiones: {c2.historial_revisiones}, Está Activo: {c2.esta_activo}".format(c2=c2))