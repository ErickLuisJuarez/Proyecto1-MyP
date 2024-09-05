import pytest
from dataset import cargar_datos_de_archivo, validar_datos, obtener_coordenadas, obtener_iata, es_iata_valido, generar_diccionario_iatas
from cache import cargar_datos_con_cache, construir_url, obtener_datos_desde_url, extraer_informacion_relevante

# Prueba para cargar datos desde un archivo
def test_cargar_datos_de_archivo():
    datos = cargar_datos_de_archivo()
    assert isinstance(datos, list), "Los datos deberían ser una lista"
    assert len(datos) > 0, "La lista de datos no debería estar vacía"

# Prueba para validar datos
def test_validar_datos():
    datos = [{'origin': 'ABC', 'destination': 'DEF', 'origin_latitude': '10.0', 'origin_longitude': '20.0',
              'destination_latitude': '30.0', 'destination_longitude': '40.0'}]
    try:
        validar_datos(datos)
    except ValueError:
        pytest.fail("validar_datos() arrojó una excepción para datos válidos")

# Prueba para obtener coordenadas
def test_obtener_coordenadas():
    datos = [{'origin': 'ABC', 'destination': 'DEF', 'origin_latitude': '10.0', 'origin_longitude': '20.0',
              'destination_latitude': '30.0', 'destination_longitude': '40.0'}]
    coordenadas = obtener_coordenadas(datos, 'ABC')
    assert coordenadas == (10.0, 20.0), "Las coordenadas no coinciden con los valores esperados"

# Prueba para verificar códigos IATA únicos
def test_obtener_iata():
    datos = [{'origin': 'ABC', 'destination': 'DEF'}, {'origin': 'GHI', 'destination': 'JKL'}]
    iatas = obtener_iata(datos)
    assert set(iatas) == {'ABC', 'DEF', 'GHI', 'JKL'}, "Los IATA obtenidos no son correctos"

# Prueba para verificar validez de un IATA
def test_es_iata_valido():
    datos = [{'origin': 'ABC', 'destination': 'DEF'}, {'origin': 'GHI', 'destination': 'JKL'}]
    assert es_iata_valido(datos, 'ABC') == True, "El IATA 'ABC' debería ser válido"
    assert es_iata_valido(datos, 'XYZ') == False, "El IATA 'XYZ' no debería ser válido"

# Prueba para generar diccionario de IATA
def test_generar_diccionario_iatas():
    datos = [{'origin': 'ABC', 'destination': 'DEF'}, {'origin': 'DEF', 'destination': 'GHI'}]
    diccionario = generar_diccionario_iatas(datos)
    assert 'ABC' in diccionario, "El diccionario debería contener el IATA 'ABC'"
    assert len(diccionario['DEF']) == 2, "El IATA 'DEF' debería tener dos registros asociados"

# Prueba para construir URL
def test_construir_url():
    url = construir_url('10.0', '20.0')
    assert "lat=10.0" in url and "lon=20.0" in url, "La URL no contiene las coordenadas correctas"

# Prueba para extraer información relevante
def test_extraer_informacion_relevante():
    json_data = {
        'current': {
            'temp': 25.0,
            'humidity': 60,
            'pressure': 1013,
            'weather': [{'description': 'clear sky'}],
            'wind_speed': 3.5
        }
    }
    info = extraer_informacion_relevante(json_data)
    assert info['temperatura_actual'] == 25.0, "La temperatura extraída no es correcta"
    assert info['humedad'] == 60, "La humedad extraída no es correcta"
    assert info['descripcion_clima'] == 'clear sky', "La descripción del clima no es correcta"
