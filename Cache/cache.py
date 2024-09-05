"""
Módulo para gestionar la carga y caché de datos desde un archivo CSV y solicitudes HTTP.

Creado por Diego Eduardo Peña Villegas 
"""

import csv
import requests
import json
import os

cache = {}

BASE_URL = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}&units=metric"
API_KEY = "a7fe8465c127fbb019e08a08ab29d0bd"
DIRECTORIO_RECURSOS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources'))
DATA_SET = os.path.join(DIRECTORIO_RECURSOS, 'dataset1.csv')


def cargar_datos_de_archivo(archivo):
    """
    Carga los datos desde un archivo CSV.

    Argumentos:
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


def construir_url(lat, lon, part='minutely,hourly,daily'):
    """
    Construye la URL completa para la solicitud a la API de OpenWeatherMap.

    Argumentos:
        lat (str): Latitud.
        lon (str): Longitud.
        part (str): Partes de la respuesta a excluir (opcional).

    Returns:
        str: URL completa para la solicitud.
    """
    return BASE_URL.format(lat=lat, lon=lon, part=part, api_key=API_KEY)

def obtener_datos_desde_url(url):
    """
    Realiza una solicitud HTTP GET a la URL especificada y devuelve la respuesta en formato JSON.

    Argumentos:
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

def extraer_informacion_relevante(json_data):
    """
    Extrae y muestra información relevante como la temperatura, humedad, y otros datos de la respuesta JSON

    Argumentos:
        json_data (dict): Respuesta JSON de la API de OpenWeatherMap.

    Returns:
        dict: Diccionario con la información extraída.
    """
    información = {
        "temperatura_actual": json_data['current']['temp'],
        "humedad": json_data['current']['humidity'],
        "presion": json_data['current']['pressure'],
        "descripcion_clima": json_data['current']['weather'][0]['description'],
        "velocidad_viento": json_data['current']['wind_speed'],
    }
    return información

def cargar_datos_con_cache(archivo):
    """
    Carga datos desde un archivo CSV y realiza solicitudes HTTP con caché para evitar duplicados.

    Argumentos:
        archivo (str): Ruta al archivo CSV.

    Returns:
        dict: Caché con los resultados de las solicitudes.
    """
    datos = cargar_datos_de_archivo(archivo)

    for fila in datos:
        lat = fila.get('lat')
        lon = fila.get('lon')
        
        if not lat or not lon:
            print(f"Coordenadas no válidas para el registro: {fila}.")
            continue
        
        cache_key = (lat, lon)

        if cache_key not in cache:
            url_completa = construir_url(lat, lon)

            try:
                json_salida = obtener_datos_desde_url(url_completa)
                cache[cache_key] = extraer_informacion_relevante(json_salida)
            except Exception as e:
                print(f"Error al obtener datos para las coordenadas {lat}, {lon}: {e}")
        else:
            print(f"Datos para las coordenadas {lat}, {lon} encontrados en caché.")

    print("Datos procesados y almacenados en caché con éxito.")
    return cache


if __name__ == "__main__":
    cache_resultado = cargar_datos_con_cache(DATA_SET)
