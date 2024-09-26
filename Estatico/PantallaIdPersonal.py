from tkinter import *
from PantallaDatos import pantalla_Datos

def pantalla_Idpersonal(window, pantalla_principal):
    """
    Muestra la pantalla para ingresar la identificación personal del usuario.
    Valida el ID ingresado y navega a la pantalla de datos si el ID es válido.

    Args:
        window (Tk): La ventana principal de la aplicación Tkinter.
        pantalla_principal (function): Función para mostrar la pantalla principal.

    """
    for widget in window.winfo_children():
        widget.destroy()

    window.title("ID_Personal")

    window.geometry("1200x600")

    imagen = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="Recursos/LogoAeropuerto.png")
    imagen.create_image(100,100, image=logo_img)
    imagen.image = logo_img
    imagen.grid(column=0, row=0)

    tituloPrincipal=Label(window, text="Personal", font=("Montserrat", 70, "bold"), fg="#011640")
    tituloPrincipal.grid(column=1, row=0, columnspan=2)

    tituloSecundario=Label(window, text="Por favor, ingresa tu identificación personal.", font=("Montserrat", 20, "bold"), fg="#011640")
    tituloSecundario.grid(column=0, row=2, columnspan=2, padx=80)

    pedirId=Label(window, text="ID:", font=("Montserrat", 15, "bold"), fg="#011526")
    pedirId.grid(column=0, row=3, sticky="E", pady=20)

    idDeEntrada = Entry(window, width=20, font=("Montserrat", 15))
    idDeEntrada.grid(column=1,row=3, sticky="W")

    mensaje_invalido = Label(window, text="", font=("Montserrat", 20), fg="red")
    mensaje_invalido.grid(column=0, row=4, columnspan=2)

    BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
    window.boton_siguiente_imagen = BotonSiguiente  
    siguiente = Button(window, image=BotonSiguiente, borderwidth=0, command=lambda:validar_id(window, idDeEntrada, mensaje_invalido))
    siguiente.grid(column=1, row=10)

    BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    window.boton_regreso_imagen = BotonRegreso 
    regreso = Button(window, image=BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=0, row=10)

    def validar_id(window, idDeEntrada, mensaje_invalido):
        """
        Valida el ID ingresado y navega a la pantalla de datos si el ID es válido.

        Args:
            window (Tk): La ventana principal de la aplicación Tkinter.
            idDeEntrada (Entry): Campo de entrada para el ID del personal.
            mensaje_invalido (Label): Etiqueta para mostrar mensajes de error.
        """
        pilot_id = idDeEntrada.get()

        if len(pilot_id) == 10:  
            mensaje_invalido.config(text="")
            pantalla_Datos(window, pantalla_principal)
        else:
            mensaje_invalido.config(text="ID incorrecto")
