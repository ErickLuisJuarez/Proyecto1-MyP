"""
Módulo para gestionar la carga y caché de datos desde un archivo CSV y solicitudes HTTP.

Creado por Diego Eduardo Peña Villegas 
"""

import csv
import requests
import json

# Diccionario para almacenar los resultados en caché
cache = {}

# Configuración de URL base y clave de API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "f269d57ff986f7ce646dd2704e7494c5"
DATA_SET = "dataset1.csv"  # Nombre del archivo de datos


def cargar_datos_de_archivo(archivo):
    """
    Carga los datos desde un archivo CSV.

    Args:
        archivo (str): Ruta al archivo CSV.

    Returns:
        list: Lista de diccionarios representando las filas del archivo CSV.
    """
    try:
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            datos = list(reader)
        print(f"Datos cargados desde {archivo} con éxito.")
        return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}.")
        raise
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        raise


def construir_url(lat, lon):
    """
    Construye la URL completa para la solicitud a la API de OpenWeatherMap.

    Args:
        lat (str): Latitud.
        lon (str): Longitud.

    Returns:
        str: URL completa para la solicitud.
    """
    return f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"


def obtener_datos_desde_url(url):
    """
    Realiza una solicitud HTTP GET a la URL especificada y devuelve la respuesta en formato JSON.

    Args:
        url (str): URL para realizar la solicitud.

    Returns:
        dict: Respuesta de la solicitud en formato JSON.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud a {url}: {e}")
        raise


def cargar_datos_con_cache(archivo):
    """
    Carga datos desde un archivo CSV y realiza solicitudes HTTP con caché para evitar duplicados.

    Args:
        archivo (str): Ruta al archivo CSV.

    Returns:
        dict: Caché con los resultados de las solicitudes.
    """
    datos = cargar_datos_de_archivo(archivo)

    for fila in datos:
        # Genera una clave para la caché basada en las coordenadas de origen
        lat = fila.get('origin_latitude')
        lon = fila.get('origin_longitude')
        
        # Verifica que lat y lon no sean nulos o vacíos antes de continuar
        if not lat or not lon:
            print(f"Coordenadas no válidas para {fila['origin']}.")
            continue
        
        cache_key = (lat, lon)

        # Verifica si la solicitud ya está en la caché
        if cache_key not in cache:
            # Construye la URL para la solicitud usando latitud y longitud
            url_completa = construir_url(lat, lon)

            # Obtiene los datos desde la URL y los guarda en la caché
            try:
                json_salida = obtener_datos_desde_url(url_completa)
                cache[cache_key] = json_salida
            except Exception as e:
                print(f"Error al obtener datos para {fila['origin']} con coordenadas {lat}, {lon}: {e}")
        else:
            print(f"Datos para {fila['origin']} con coordenadas {lat}, {lon} encontrados en caché.")

    print("Datos procesados y almacenados en caché con éxito.")
    return cache


# Para ejecutar el script directamente y cargar los datos con caché
if __name__ == "__main__":
    # Cargar datos y procesar con caché
    cache_resultado = cargar_datos_con_cache(DATA_SET)