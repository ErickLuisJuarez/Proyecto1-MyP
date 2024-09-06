from tkinter import *
from PantallaPersonalDatos import pantalla_personal_datos

def pantalla_personal(window, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Personal")

    window.geometry("1200x500")

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
    window.boton_siguiente_imagen = BotonSiguiente  # guardamos la referencia a la imagen
    siguiente = Button(window, image=BotonSiguiente, borderwidth=0, command=lambda:validar_id(window, idDeEntrada, mensaje_invalido))
    siguiente.grid(column=1, row=10)

    BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    window.boton_regreso_imagen = BotonRegreso  # guardamos la referencia a la imagen
    regreso = Button(window, image=BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=0, row=10)

    def validar_id(window, idDeEntrada, mensaje_invalido):
        pilot_id = idDeEntrada.get()

        if len(pilot_id) == 10:  # el ID del personal siempre es de 10 caracteres
            mensaje_invalido.config(text="")
            pantalla_personal_datos(window, pantalla_principal)
        else:
            mensaje_invalido.config(text="ID incorrecto")
