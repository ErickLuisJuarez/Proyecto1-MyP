"""
Código que gestiona y procesa los datos del archivo dataset1.cvs

Creado por Erick Luis Juárez
"""

import cache
import csv

def cargar_datos_de_archivo():
    """
    Carga los datos desde el archivo CSV utilizando la funcionalidad de caché.

    Returns:
        list: Lista de diccionarios representando las filas del archivo CSV.
    """
    try:
        datos = cache.cargar_datos_de_archivo(cache.DATA_SET)
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        raise

def validar_datos(datos):
    """
    Valida los datos cargados del archivo CSV.

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Raises:
        ValueError: Si los datos no son válidos.
    """
    for fila in datos:
        for columna, tipo in [('origin_latitude', float), ('origin_longitude', float),
                             ('destination_latitude', float), ('destination_longitude', float)]:
            try:
                float(fila[columna])
            except ValueError:
                raise ValueError(f"El valor en la columna '{columna}' debe ser un número.")
        if any(fila[col] == '' for col in ['origin', 'destination', 'origin_latitude', 'origin_longitude', 'destination_latitude', 'destination_longitude']):
            raise ValueError("El archivo contiene valores nulos.")
    print("Datos validados con éxito.")

def obtener_coordenadas(datos, iata):
    """
    Obtiene las coordenadas asociadas a un código IATA.

    Args:
        datos (list): Lista de diccionarios con datos de vuelos.
        iata (str): Código IATA para buscar.

    Returns:
        tuple: Latitud y longitud si se encuentra el IATA, None si no.
    """
    for fila in datos:
        if fila['origin'] == iata:
            return fila['origin_latitude'], fila['origin_longitude']
        elif fila['destination'] == iata:
            return fila['destination_latitude'], fila['destination_longitude']

    return None

def obtener_iata(datos):
    """
    Obtiene una lista de todos los códigos IATA únicos en los datos.

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        list: Lista de códigos IATA únicos.
    """
    iatas_origen = set()
    iatas_destino = set()
    for fila in datos:
        iatas_origen.add(fila['origin'])
        iatas_destino.add(fila['destination'])
    return list(iatas_origen.union(iatas_destino))

def es_iata_valido(datos, iata):
    """
    Verifica si un código IATA es válido en los datos
    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV
        iata (str): Código IATA a verificar.

    Returns:
        bool: True si el IATA es válido, False en caso contrario
    """
    for fila in datos:
        if fila['origin'] == iata or fila['destination'] == iata:
            return True
    return False

def generar_diccionario_iatas(datos):
    """Genera un diccionario con las IATA como claves y sus registros como valores
    
    Args:
        datos (list): Lista de diccionarios, donde cada diccionario representa una fila 
                      del archivo CSV con las claves 'origin', 'destination', 'origin_latitude', 
                      'origin_longitude', 'destination_latitude', 'destination_longitude', etc.

    Returns:
        dict: Un diccionario donde las claves son códigos IATA (str) y los valores son 
              listas de diccionarios que contienen los registros asociados a cada código IATA.

    """
    diccionario_iatas = {}
    for fila in datos:
        iata_origen = fila['origin']
        iata_destino = fila['destination']
        if iata_origen not in diccionario_iatas:
            diccionario_iatas[iata_origen] = []
        if iata_destino not in diccionario_iatas:
            diccionario_iatas[iata_destino] = []
        diccionario_iatas[iata_origen].append(fila)
        diccionario_iatas[iata_destino].append(fila)
    return diccionario_iatas

def crear_diccionario_ciudades():
    """
    Crea un diccionario que asocia códigos IATA con nombres de ciudades.

    La función primero lee un archivo CSV que contiene información de vuelos 
    para extraer los códigos IATA (campo 1). Luego, empareja estos códigos IATA 
    con una lista predefinida de tuplas que relacionan códigos IATA con los 
    nombres de las ciudades correspondientes.

    Returns:
        dict: Un diccionario donde las claves son códigos IATA (str) y los 
              valores son los nombres de las ciudades (str) asociadas a esos códigos.
    """
    iatas = []
    
    with open(cache.DATA_SET, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)

        for fila in lector:
            iata = fila[1] 
            if iata not in iatas: 
                iatas.append(iata) 
    #aqui estaba la lista de iatas y ciudades

    diccionario_ciudades = {}
    for iata in iatas:
        for iata_ciudad in iatas_y_ciudades:
            if iata == iata_ciudad[0]: 
                diccionario_ciudades[iata] = iata_ciudad[1]
    
    return diccionario_ciudades

def obtener_nombre_ciudad_por_iata(iata):
    """
    Obtiene el nombre de la ciudad a partir del código IATA.

    Args:
        iata (str): Código IATA de la ciudad.

    Returns:
        str: Nombre de la ciudad correspondiente al código IATA.
    """
    diccionario_ciudades = crear_diccionario_ciudades()
    return diccionario_ciudades.get(iata, None)