from tkinter import *
from PantallaClima import pantalla_clima
import dataset

def pantalla_principal(window):
    """
    Esta es la pantalla principal de inicio al ejecutar le programa de consulta de clima.

    Parámetros:
    window (Tk): La ventana principal de Tkinter en la que se colocan todos los widgets.

    Descripción:
    - Primero limpia todos los widgets existentes en la ventana.
    - Se hace la configuración del título y el tamaño de la ventana.
    - Se crea un lienzo para mostrar la imagen dellogo del aeropuerto.
    - Se agregan títulos y botones para que el usuario seleccione su rol y se pueda avanzar a las siguientes ventanas.
    """
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Consulta de clima")
    window.minsize(width=100, height=700)
    window.config(padx=20, pady=20)
    
    lienzo = Canvas(window, width=200, height=200) 
    window.logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo.create_image(100, 100, image=window.logoaeropuerto)
    lienzo.grid(column=0, row=0)

    titulo1=Label(text="Consulta de clima", font=("Montserrat", 80, "bold"), fg="#011640")
    titulo1.grid(column=1, row=0)

    titulo2 = Label(window, text="Introduzca IATA, Ciudad  o Ticket \n para realizar la busqueda", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
    titulo2.grid(column=0, row=1, columnspan=3, padx=150, pady=50, sticky="n")

    Pedir_datos = Label(window, text="Datos:", font=("Montserrat", 20, "bold"), fg="#026773")
    Pedir_datos.grid(column=0, row=2, pady=15)
    Datos_entrada = Entry(window, width=20, font=("Montserrat", 15))
    Datos_entrada.grid(column=1, row=2)

    mensaje_invalido = Label(window, text="", font=("Montserrat", 20), fg="red")
    mensaje_invalido.grid(column=0, row=3, columnspan=2)

    BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png")
    window.boton_siguiente_imagen = BotonSiguiente
    siguiente = Button(window, image=BotonSiguiente, borderwidth=0, command=lambda: validar_datos(window, Datos_entrada.get(), mensaje_invalido))
    siguiente.grid(column=1, row=4, pady=50)

    def validar_datos(window, datos, mensaje_invalido):
        """
        Valida la longitud de la entrada de datos. Debe tener entre 3 y 10 caracteres.

        Args:
            window (Tk): La ventana principal de la aplicación Tkinter.
            datos (str): Entrada de datos del usuario (código IATA, ciudad o ticket).
            mensaje_invalido (Label): Etiqueta para mostrar mensajes de error.
        """
        print(f"Datos ingresados: {datos}")

        if 3 <= len(datos) <= 10:
            mensaje_invalido.config(text="")
            print("Datos válidos. Avanzando a la siguiente pantalla.") 
            pantalla_clima(window, pantalla_principal)
        else:
            mensaje_invalido.config(text="Los datos deben tener entre 3 y 10 caracteres")
            print("Datos inválidos. Por favor, ingrese datos válidos.")

window = Tk()
pantalla_principal(window)
window.mainloop()