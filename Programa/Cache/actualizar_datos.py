import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from cache import cargar_datos_con_cache, DATA_SET

def actualizar_info():
    """
    Ejecuta la actualización de datos desde el archivo CSV y API.
    """
    print("Iniciando la actualización de datos...")
    resultado_cache = cargar_datos_con_cache(DATA_SET)

    print("Actualización completada.")

if __name__ == "__main__":
    actualizar_info()
