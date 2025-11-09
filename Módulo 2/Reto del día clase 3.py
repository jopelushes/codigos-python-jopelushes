# Reto del día clase 3
# Módulo 2
# Autor: Jonathan Perulles Cárdenas
# Fecha: 29 de octubre de 2025

# Clase padre generica
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        # Definiendo atributos adicionales
        self.kilometraje = 0
        self._encendido = False
        pass
    def arrancar(self):
        if self._encendido == False:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha sido encendido")
        else:
            print("El vehículo ya estaba encendido")
    def apagar(self):
        if self._encendido == True:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} ha sido apagado")
        else:
            print("El vehículo ya estaba apagado")
    def get_kilometraje(self):
        return self.kilometraje
    def mostrar_info_base(self):
        print(f"Vehículo marca {self.marca}, modelo {self.modelo} del año {self.anio}")

# Clase hija
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
    def conducir(self, km):
        if self._encendido == True:
            try:
                self.kilometraje += km
                print(f"Conduciendo {km} km...")
            except ValueError:
                print("Ingresa un número válido")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Error: El coche debe estar arrancado para conducir.")

class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0
    def cargar(self, kilos):
        try:
            cantidad_kilos = float(kilos)
            if cantidad_kilos < self.capacidad_carga_kg - self.__carga_actual_kg:
                self.__carga_actual_kg += cantidad_kilos
                print("Carga exitosa")
            else:
                print("Error de sobrecarga")
        except ValueError:
            print("Ingresa un número válido")
        except Exception as e:
            print(f"Error: {e}")
    def descargar(self, kilos):
        try:
            cantidad_kilos = float(kilos)
            if cantidad_kilos < self.capacidad_carga_kg:
                self.__carga_actual_kg -= cantidad_kilos
                print("Descarga exitosa")
            else:
                print("La cantidad supera a la carga actual")
        except ValueError:
            print("Ingresa un número válido")
        except Exception as e:
            print(f"Error: {e}")
    def get_carga_actual(self):
        return self.__carga_actual_kg
    
# Creando objetos
mi_coche = Coche("Porsche", "Cayanne", 2025, 4)
mi_camion = Camion("DAF", "XB", 2025, 5000)

# Probando los vehículos
print("\n== Datos del camión ==")
mi_coche.mostrar_info_base()
print(f"Mi coche tiene {mi_coche.num_puertas} puertas")

print("\n== Prueba del coche ==")
mi_coche.conducir(100)
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()
print(f"Kilometraje (getter): {mi_coche.get_kilometraje()} km")

print("\n== Datos del camión ==")
mi_camion.mostrar_info_base()
print(f"Capacidad: {mi_camion.capacidad_carga_kg} kg")

print("\n== Prueba del camión ==")
mi_camion.cargar(3000)           
mi_camion.cargar(3000)            
mi_camion.descargar(1000)         
print(f"Carga actual (getter): {mi_camion.get_carga_actual()} kg")


    