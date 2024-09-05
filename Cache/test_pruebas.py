import pytest
from unittest.mock import patch, MagicMock
from dataset import (
    cargar_datos_de_archivo,
    validar_datos,
    obtener_coordenadas,
    obtener_iata,
    es_iata_valido,
    generar_diccionario_iatas
)
from cache import cargar_datos_con_cache, extraer_informacion_relevante, obtener_datos_desde_url, construir_url


@patch('dataset.cache.cargar_datos_de_archivo')
def test_cargar_datos_de_archivo(mock_cargar):
    # Mocking dataset to return a fake response
    mock_cargar.return_value = [
        {'origin': 'JFK', 'destination': 'LAX', 'origin_latitude': '40.6413', 'origin_longitude': '-73.7781',
         'destination_latitude': '33.9416', 'destination_longitude': '-118.4085'}
    ]
    datos = cargar_datos_de_archivo()
    assert len(datos) == 1
    assert datos[0]['origin'] == 'JFK'


def test_validar_datos():
    # Valid data
    datos_validos = [
        {'origin': 'JFK', 'destination': 'LAX', 'origin_latitude': '40.6413', 'origin_longitude': '-73.7781',
         'destination_latitude': '33.9416', 'destination_longitude': '-118.4085'}
    ]
    # This should not raise an exception
    validar_datos(datos_validos)

    # Invalid data
    datos_invalidos = [
        {'origin': 'JFK', 'destination': 'LAX', 'origin_latitude': 'NaN', 'origin_longitude': '-73.7781',
         'destination_latitude': '33.9416', 'destination_longitude': '-118.4085'}
    ]
    with pytest.raises(ValueError):
        validar_datos(datos_invalidos)


def test_obtener_coordenadas():
    datos = [
        {'origin': 'JFK', 'destination': 'LAX', 'origin_latitude': '40.6413', 'origin_longitude': '-73.7781',
         'destination_latitude': '33.9416', 'destination_longitude': '-118.4085'}
    ]
    coordenadas = obtener_coordenadas(datos, 'JFK')
    assert coordenadas == (40.6413, -73.7781)


def test_es_iata_valido():
    datos = [
        {'origin': 'JFK', 'destination': 'LAX', 'origin_latitude': '40.6413', 'origin_longitude': '-73.7781',
         'destination_latitude': '33.9416', 'destination_longitude': '-118.4085'}
    ]
    assert es_iata_valido(datos, 'JFK')
    assert not es_iata_valido(datos, 'XXX')


@patch('cache.requests.get')
def test_obtener_datos_desde_url(mock_get):
    # Mock the HTTP response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "current": {
            "temp": 20,
            "humidity": 50,
            "pressure": 1012,
            "weather": [{"description": "clear sky"}],
            "wind_speed": 5
        }
    }
    mock_get.return_value = mock_response

    url = construir_url('40.7128', '-74.0060')
    datos = obtener_datos_desde_url(url)
    assert datos['current']['temp'] == 20


def test_extraer_informacion_relevante():
    json_data = {
        "current": {
            "temp": 20,
            "humidity": 50,
            "pressure": 1012,
            "weather": [{"description": "clear sky"}],
            "wind_speed": 5
        }
    }
    info = extraer_informacion_relevante(json_data)
    assert info['temperatura_actual'] == 20
    assert info['humedad'] == 50


@patch('cache.cargar_datos_de_archivo')
@patch('cache.obtener_datos_desde_url')
def test_cargar_datos_con_cache(mock_obtener_datos, mock_cargar_datos):
    mock_cargar_datos.return_value = [
        {'lat': '40.7128', 'lon': '-74.0060'}
    ]
    mock_obtener_datos.return_value = {
        "current": {
            "temp": 20,
            "humidity": 50,
            "pressure": 1012,
            "weather": [{"description": "clear sky"}],
            "wind_speed": 5
        }
    }
    cache = cargar_datos_con_cache('dummy_path.csv')
    assert ('40.7128', '-74.0060') in cache
    assert cache[('40.7128', '-74.0060')]['temperatura_actual'] == 20
