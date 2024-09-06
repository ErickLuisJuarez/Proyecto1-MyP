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
    
# Prueba para cargar_datos_con_cache
def test_cargar_datos_con_cache(mocker):
    # Simulamos que el archivo se lee correctamente y los datos se cachean
    mock_datos = [{'origin': 'ABC', 'destination': 'DEF'}]
    
    # Simulamos la función que carga datos directamente del archivo
    mocker.patch('cache.cargar_datos_de_archivo', return_value=mock_datos)
    
    # La primera vez se debe cargar desde el archivo
    datos = cargar_datos_con_cache('dataset1.csv')
    assert datos == mock_datos, "Los datos deberían ser los esperados del archivo"

    # Ahora cacheamos la respuesta para una segunda llamada
    mocker.patch('cache.leer_cache', return_value=mock_datos)
    datos_cacheados = cargar_datos_con_cache('dataset1.csv')
    assert datos_cacheados == mock_datos, "Los datos deberían ser los mismos que los cacheados"
    
# Prueba para obtener_datos_desde_url
def test_obtener_datos_desde_url(mocker):
    # Simulamos una respuesta exitosa de la URL
    mock_response = {
        'current': {
            'temp': 22.0,
            'humidity': 80,
            'pressure': 1012,
            'weather': [{'description': 'clear sky'}],
            'wind_speed': 5.0
        }
    }
    
    # Simulamos que requests.get devuelve un mock de respuesta con un JSON
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: mock_response))
    
    # Llamamos a la función con una URL simulada
    datos = obtener_datos_desde_url('https://fakeurl.com')
    
    # Verificamos que los datos retornados coinciden con lo esperado
    assert datos['current']['temp'] == 22.0, "La temperatura obtenida no es la esperada"
    assert datos['current']['humidity'] == 80, "La humedad obtenida no es la esperada"
    assert datos['current']['weather'][0]['description'] == 'clear sky', "La descripción del clima no es la esperada"