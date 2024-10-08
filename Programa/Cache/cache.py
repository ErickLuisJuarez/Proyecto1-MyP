"""
Módulo para gestionar la carga y caché de datos desde un archivo CSV y solicitudes HTTP.

"""

import csv
import requests
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import credenciales

dir_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
carpeta_csv = os.path.join(dir_base, '..', 'Estatico', 'CSV')
DATA_SET = os.path.join(carpeta_csv, 'dataset1- v2 con tickets resumidos - dataset1.csv')

 
cache = {}



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


def construir_url(ciudad):
    """
    Construye la URL para obtener datos climáticos desde la API.
    """
    return f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={credenciales.API_KEY}&units=metric'

def construir_url_por_coordenadas(latitud, longitud):
    """
    Construye la URL para obtener datos climáticos desde la API utilizando coordenadas.
    """
    return f'http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={credenciales.API_KEY}&units=metric'

    
def obtener_datos_desde_url(url):
    """
    Obtiene datos desde una URL.

    Args:
        url (str): URL desde la que se obtienen los datos.

    Returns:
        dict: Datos en formato JSON obtenidos de la URL.
    """
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.HTTPError as http_err:
        return {'error': f'Error HTTP: {http_err}'}
    except Exception as err:
        return {'error': f'Error: {err}'}

def extraer_informacion_relevante(json_data):
    """
    Extrae información relevante del JSON de respuesta de la API de OpenWeatherMap.

    Args:
        json_data (dict): Respuesta JSON de la API de OpenWeatherMap.

    Returns:
        dict: Un diccionario con la temperatura, presión, humedad, velocidad del viento,
              y probabilidad de lluvia.
    """
    try:
        temperatura = json_data['main']['temp']
        presion = json_data['main']['pressure']
        humedad = json_data['main']['humidity']
        velocidad_viento = json_data['wind']['speed']
        probabilidad_lluvia = json_data.get('rain', {}).get('1h', 0)

        return {
            'temperatura': temperatura,
            'presion': presion,
            'humedad': humedad,
            'velocidad_viento': velocidad_viento,
            'probabilidad_lluvia': probabilidad_lluvia
        }
    except KeyError as e:
        print(f"Error al extraer datos: {e}")
        return {'error': 'Datos incompletos o respuesta de API no válida'}

def cargar_datos_con_cache(archivo):
    """
    Carga datos desde un archivo CSV y realiza solicitudes HTTP con caché para evitar duplicados.

    Argumentos:
        archivo (str): Ruta al archivo CSV.

    Returns:
        dict: Caché con los resultados de las solicitudes.
    """
    datos = cargar_datos_de_archivo(archivo)

    cache_local = {}

    for fila in datos:
        latitud1 = fila.get('origin_latitude')
        longitud1 = fila.get('origin_longitude')
        
        if not latitud1 or not longitud1:
            print(f"Coordenadas no validas para el registro: {fila}.")
            continue
        
        cache_key = (latitud1, longitud1)

        if cache_key not in cache_local:
            url_completa = construir_url_por_coordenadas(latitud1, longitud1)

            try:
                json_salida = obtener_datos_desde_url(url_completa)
                cache_local[cache_key] = extraer_informacion_relevante(json_salida)
            except Exception as e:
                print(f"Error al obtener datos para las coordenadas {latitud1}, {longitud1}: {e}")
        else:
            print(f"Datos para las coordenadas {latitud1}, {longitud1} encontrados en caché.")

    print("Datos procesados y almacenados en caché con éxito.")
    return {'registros': cache_local}

if __name__ == "__main__":
    cache_resultado = cargar_datos_con_cache(DATA_SET)