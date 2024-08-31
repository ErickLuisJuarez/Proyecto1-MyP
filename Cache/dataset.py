"""
Código que gestiona y procesa los datos del archivo dataset1.cvs

Creado por Erick Luis Juárez
"""

# Se importa el código cache de la carpeta Cache
import cache

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
    """
    Obtiene las coordenadas asociadas a un IATA dado.

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.
        iata (str): Código IATA.

    Returns:
        tuple: Tupla de coordenadas (latitud, longitud) si se encuentra el IATA, None en caso contrario.
    """
    for fila in datos:
        if fila['origin'] == iata:
            return (float(fila['origin_latitude']), float(fila['origin_longitude']))
        elif fila['destination'] == iata:
            return (float(fila['destination_latitude']), float(fila['destination_longitude']))
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

def obtener_nombres(datos):
    """
    Obtiene una lista de nombres únicos (códigos IATA de origen y destino)

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.

    Returns:
        list: Lista de nombres únicos.
    """
    nombres = set()
    for fila in datos:
        nombres.add(fila['origin'])
        nombres.add(fila['destination'])
    return list(nombres)

def nombre_valido(datos, nombre):
    """
    Verifica si un nombre (código IATA) es válido en los datos

    Args:
        datos (list): Lista de diccionarios representando las filas del archivo CSV.
        nombre (str): Nombre a verificar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario
    """
    return nombre in obtener_nombres(datos)

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