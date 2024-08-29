"""
Código que gestiona y procesa los datos del archivo dataset1.cvs

Creado por Erick Luis Juárez
"""
# Se importa el módulo csv para manejo de archivos CSV
import csv
# Se importa el código cache de la carpeta Cache
from Cache import cache

def cargar_datos_de_archivo():
    try:
        with open(cache.DATA_SET, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)
            # Validación básica: verificar si hay filas
            if not datos:
                raise ValueError("El archivo está vacío.")
            return datos
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo {cache.DATA_SET}")
    except csv.Error as error:
        raise ValueError(f"Error al leer el archivo CSV: {error}")

def validar_datos(datos):
    for fila in datos:
        # Validar tipo de datos para columnas numéricas
        for columna, tipo in [('origin_latitude', float), ('origin_longitude', float),
                             ('destination_latitude', float), ('destination_longitude', float)]:
            try:
                float(fila[columna])
            except ValueError:
                raise ValueError(f"El valor en la columna '{columna}' debe ser un número.")
        # Validar valores nulos en columnas clave
        if any(fila[col] == '' for col in ['origin', 'destination', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude']):
            raise ValueError("El archivo contiene valores nulos.")
    print("Datos validados con éxito.")

def obtener_coordenadas(datos, iata):
    for fila in datos:
        if fila['origin'] == iata:
            return (float(fila['origin_latitude']), float(fila['origin_longitude']))
        elif fila['destination'] == iata:
            return (float(fila['destination_latitude']), float(fila['destination_longitude']))
    return None

def obtener_iata(datos):
    iatas_origen = set()
    iatas_destino = set()
    for fila in datos:
        iatas_origen.add(fila['origin'])
        iatas_destino.add(fila['destination'])
    return list(iatas_origen.union(iatas_destino))

def es_iata_valido(datos, iata):
    for fila in datos:
        if fila['origin'] == iata or fila['destination'] == iata:
            return True
    return False

def obtener_nombres(datos):
    nombres = set()
    for fila in datos:
        nombres.add(fila['origin'])
        nombres.add(fila['destination'])
    return list(nombres)

def nombre_valido(datos, nombre):
    return nombre in obtener_nombres(datos)