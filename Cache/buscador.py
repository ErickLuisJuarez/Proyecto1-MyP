"""
Código que sirve como buscador para consultar
y buscar información almacenada en el cache.

Creado por Erick Luis Juárez
"""
import datetime
import cache
from dataset import cargar_datos_de_archivo, validar_datos, generar_diccionario_iatas

def cargar_datos_y_generar_busqueda():
    """
    Carga los datos desde el archivo CSV, valida los datos y genera el diccionario para la búsqueda.

    Returns:
        dict: Diccionario donde cada clave es un código IATA y el valor es una lista de registros asociados.
    """
    try:
        datos = cargar_datos_de_archivo()
        validar_datos(datos)
        return generar_diccionario_iatas(datos)
    except FileNotFoundError:
        print(f"El archivo {cache.DATA_SET} no se encontró.")
    except ValueError as ve:
        print(f"Error de validación de datos: {ve}")
    except KeyError as ke:
        print(f"Clave faltante en los datos: {ke}")
    except Exception as e:
        print(f"Error al cargar y generar datos: {e}")
    return {}

def obtener_datos_climaticos(registros: dict, cache_clima: dict, iata_origen: str = '', iata_destino: str = ''):
    """
    Obtiene una lista con los datos climáticos y de ubicación necesarios para mostrar en los registros de búsqueda.

    La función consulta el cache de clima y los registros del dataset para consolidar la información sobre clima
    para los códigos IATA de origen y destino.

    Parámetros:
        *registros: dict
            Diccionario que mapea números de tickets a listas de códigos IATA de origen y destino.
        *cache_clima: dict
            Diccionario con datos de clima almacenados en caché.
        *iata_origen: str
            Código IATA de origen.
        *iata_destino: str
            Código IATA de destino.

    Retorna:
        *lista_datos: list
            Lista con formato [iata_origen:str, lat_origen:float, lon_origen:float, clima_origen:str,
            rango_temperatura_origen:str, humedad_origen:str, iata_destino:str, lat_destino:float,
            lon_destino:float, clima_destino:str, rango_temperatura_destino:str, humedad_destino:str].
    """
    lista_datos = []
    hora_actual = datetime.datetime.now().hour

    try:
        if cache_clima == registros or iata_origen == iata_destino:
            lista_datos.extend(['NULL'] * 6 + ['NULL'] * 6)
        else:
            for i in range(hora_actual, 24):
                if cache_clima['registros'][iata_origen][i] != ['NULL'] * 5:
                    hora_actual = i
                    break

            clima_origen = f"{cache_clima['registros'][iata_origen][hora_actual][1]} / {cache_clima['registros'][iata_origen][hora_actual][2]}"
            lista_datos.extend([
                iata_origen,
                registros[iata_origen][0],
                registros[iata_origen][1],
                cache_clima['registros'][iata_origen][hora_actual][0],
                clima_origen,
                cache_clima['registros'][iata_origen][hora_actual][3]
            ])

            if hora_actual < 22:
                clima_destino = f"{cache_clima['registros'][iata_origen][hora_actual + 2][1]} / {cache_clima['registros'][iata_origen][hora_actual + 2][2]}"
                lista_datos.extend([
                    iata_destino,
                    registros[iata_destino][0],
                    registros[iata_destino][1],
                    cache_clima['registros'][iata_destino][hora_actual + 2][0],
                    clima_destino,
                    cache_clima['registros'][iata_origen][hora_actual + 2][3]
                ])
            else:
                clima_destino = f"{cache_clima['registros'][iata_origen][23][1]} / {cache_clima['registros'][iata_origen][23][2]}"
                lista_datos.extend([
                    iata_destino,
                    registros[iata_destino][0],
                    registros[iata_destino][1],
                    cache_clima['registros'][iata_destino][23][0],
                    clima_destino,
                    cache_clima['registros'][iata_origen][23][3]
                ])
    except KeyError as ke:
        print(f"Clave faltante en el cache de clima o registros: {ke}")
    except IndexError as ie:
        print(f"Índice fuera de rango al acceder a los datos climáticos: {ie}")
    except Exception as e:
        print(f"Error al obtener los datos climáticos: {e}")

    return lista_datos

def encontrar_iata_por_nombre(nombre_ciudad, diccionario_iatas):
    """
    Encuentra el código IATA correspondiente al nombre de la ciudad o aeropuerto dado.

    Args:
        nombre_ciudad (str): Nombre de la ciudad o aeropuerto.
        diccionario_iatas (dict): Diccionario con los datos organizados por IATA.

    Returns:
        str: Código IATA correspondiente al nombre de la ciudad o aeropuerto, o None si no se encuentra.
    """
    if not nombre_ciudad:
        print("El nombre de la ciudad no puede estar vacío.")
        return None

    nombre_ciudad = nombre_ciudad.lower()
    try:
        for iata, registros in diccionario_iatas.items():
            for registro in registros:
                nombre_completo = registro.get('city_name', '').lower()
                if nombre_ciudad in nombre_completo or nombre_completo in nombre_ciudad:
                    return iata
    except KeyError as ke:
        print(f"Clave faltante en el diccionario de IATA: {ke}")
    except Exception as e:
        print(f"Error al encontrar el código IATA: {e}")

    print(f"No se encontró un código IATA para: {nombre_ciudad}")
    return None

def buscar_vuelos_por_ciudad(origen_ciudad, destino_ciudad, diccionario_iatas):
    """
    Realiza una búsqueda de vuelos según el nombre de la ciudad o aeropuerto de origen y destino.

    Args:
        origen_ciudad (str): Nombre de la ciudad o aeropuerto de origen.
        destino_ciudad (str): Nombre de la ciudad o aeropuerto de destino.
        diccionario_iatas (dict): Diccionario con los datos organizados por IATA.

    Returns:
        list: Lista de registros que coinciden con los criterios de búsqueda, o una lista vacía si no se encuentra.
    """
    try:
        origen_iata = encontrar_iata_por_nombre(origen_ciudad, diccionario_iatas)
        destino_iata = encontrar_iata_por_nombre(destino_ciudad, diccionario_iatas)

        if not origen_iata or not destino_iata:
            return []

        return buscar_vuelos(origen_iata, destino_iata, diccionario_iatas)
    except Exception as e:
        print(f"Error al buscar vuelos: {e}")
        return []

def buscar_vuelos(origen, destino, diccionario_iatas):
    """
    Realiza una búsqueda de vuelos según el origen y destino IATA.

    Args:
        origen (str): Código IATA de origen.
        destino (str): Código IATA de destino.
        diccionario_iatas (dict): Diccionario con los datos organizados por IATA.

    Returns:
        list: Lista de registros que coinciden con los criterios de búsqueda.
    """
    try:
        vuelos = []
        registros_origen = diccionario_iatas.get(origen, [])
        for registro in registros_origen:
            if registro.get('destination') == destino:
                vuelos.append(registro)
        return vuelos
    except KeyError as keyerror:
        print(f"Clave faltante en el registro: {keyerror}")
    except Exception as error:
        print(f"Error inesperado al buscar vuelos: {error}")
    return []

if __name__ == "__main__":
    diccionario_iatas = cargar_datos_y_generar_busqueda()