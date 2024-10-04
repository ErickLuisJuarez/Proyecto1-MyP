import os
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cache
from Cache import buscador
from Cache import dataset

dir_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
carpeta_csv = os.path.join(dir_base, '..', 'Estatico', 'CSV')
DATA_SET = os.path.join(carpeta_csv, 'dataset1- v2 con tickets resumidos - dataset1.csv')
IATA_CIUDAD_CSV = os.path.join(carpeta_csv, 'IATA-Ciudad.csv')

def test_cargar_datos_de_archivo():
    datos = cache.cargar_datos_de_archivo(DATA_SET)
    assert isinstance(datos, list)
    assert len(datos) > 0 

def test_construir_url():
    ciudad = 'Mexico City'
    url = cache.construir_url(ciudad)
    assert 'Mexico City' in url
    assert 'appid=' in url

def test_extraer_informacion_relevante():
    json_data = {
        "main": {
            "temp": 22,
            "pressure": 1015,
            "humidity": 60
        },
        "wind": {
            "speed": 3.5
        },
        "rain": {
            "1h": 1.2
        }
    }
    datos_relevantes = cache.extraer_informacion_relevante(json_data)
    assert datos_relevantes['temperatura'] == 22
    assert datos_relevantes['probabilidad_lluvia'] == 1.2

def test_cargar_datos_con_cache():
    resultado_cache = cache.cargar_datos_con_cache(DATA_SET) 
    assert isinstance(resultado_cache, dict)
    assert 'registros' in resultado_cache 
    assert len(resultado_cache['registros']) > 0  


def test_corregir_nombre_ciudad():
    dataset.crear_diccionario_ciudades() 
    iata, sugerencia = buscador.corregir_nombre_ciudad("ciudad de mexico")
    assert iata == "MEX" 
    assert sugerencia is None

def test_corregir_codigo_iata():
    dataset.crear_diccionario_ciudades() 
    iata, sugerencia = buscador.corregir_codigo_iata("MEX")
    assert iata == "MEX"
    assert sugerencia is None

def test_obtener_datos_climaticos_por_ciudad():
    dataset.crear_diccionario_ciudades()
    ciudad = "Ciudad de México" 
    datos_climaticos = buscador.obtener_datos_climaticos_por_ciudad(ciudad, [])
    assert datos_climaticos is not None, "Los datos climáticos no deben ser None"

def test_identificar_tipo_entrada():
    assert buscador.identificar_tipo_entrada("MEX") == 'iata'
    assert buscador.identificar_tipo_entrada("Mexico City") == 'ciudad'
    assert buscador.identificar_tipo_entrada("AT1M21") == 'ticket'