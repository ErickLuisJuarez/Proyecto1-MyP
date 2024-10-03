Proyecto1-MyP: Información del Clima para el AICM
Aplicación para consultar información del clima diseñada para el personal y clientes del Aeropuerto Internacional de la Ciudad de México.

#Requisitos:
Python 3.8 o superior
Tkinter (para la interfaz gráfica)
Pytest (para las pruebas)

#Instalación: Sigue estos pasos para instalar las dependencias necesarias en terminal
Instalar tkinter para la interfaz gráfica con el comando $ sudo apt-get install python3-tk
Instalar pip (si aún no está instalado) con el comando $ sudo apt-get install python3-pip
Instalar pytest para ejecutar las pruebas con el comando $ sudo pip3 install pytest

#Uso: Para ejecutar la aplicación, sigue estos pasos
Descarga los archivos del proyecto o clona el repositorio con el comando $ git clone https://github.com/ErickLuisJuarez/Proyecto1-MyP.git desde la carpeta de tu elección
Descarga el archivo credenciales.py que te fue proporcionado individualmente
Navega al proyecto con el comando $ cd Proyecto1-MyP
Navega a la carpeta Programa con el comando $ cd Programa
Navega a la carpeta Cache con el comando $ cd Cache
Mueve el archivo credenciales.py a esta carpeta
Vuelve a la carpeta Programa y ejecuta la aplicación con el comando $ python3 interfaz.py
Sigue las instrucciones en pantalla: En la parte derecha, puedes hacer click sobre la imagen que desees. La de arriba te abrirá la página de Aeroméxico para poder realizar la compra de un boleto de avión. La de abajo te abrirá la página de Trivago para reservar una habitación de hotel. En el cuadro de texto de la aplicación del clima, introduce un código IATA, el nombre de una ciudad o tu ticket de vuelo. Haz click en el botón siguiente para consultar la información del clima correspondiente. Una vez en la pantalla con los datos, desplázate con la barra deslizadora para visualizar toda la información. Al terminar, haz click en el botón de regreso para realizar otra búsqueda, o cierra la aplicación si ya no deseas realizar más búsquedas.

#Ejecutar Tests: Para ejecutar las pruebas del proyecto
Verifica que pytest esté instalado (si no, sigue los pasos de instalación arriba).
Navega a la carpeta Cache con el comando $ cd Cache
Ejecuta los tests con el comando $ pytest

#Integrantes del equipo y sus roles:
Líder del equipo: Diego Eduardo Peña Villegas
Frontend: Brenda Rodríguez Jiménez, Oscar Iván Sánchez González, Tomás Barrera Hernández
Backend: Luis Juárez Erick, Diego Eduardo Peña Villegas
