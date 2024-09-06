from tkinter import *
from PantallaRecomendacionesPersonal import pantalla_recomendaciones_personal

def pantalla_personal_datos(window, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Personal")
    window.minsize(width=800, height=800)
    window.config(padx=20, pady=20)

    lienzo = Canvas(window, width=200, height=200)
    logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo.create_image(100, 100, image=logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    tituloPrincipal = Label(window, text="Personal", font=("Montserrat", 60, "bold"), fg="#011640")
    tituloPrincipal.grid(column=1, row=0, pady=20, sticky="w")

    tituloSecundario = Label(window, text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
    tituloSecundario.grid(column=0, row=1, columnspan=3, padx=150, sticky="n", pady=15)

    Origen = Label(window, text="Origen", font=("Montserrat", 20, "bold"), fg="#026773")
    Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
    entradaOrigen = Entry(window, width=20, font=("Montserrat", 15))
    entradaOrigen.grid(column=1, row=3)

    Destino = Label(window, text="Destino", font=("Montserrat", 20, "bold"), fg="#026773")
    Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
    entradaDestino = Entry(window, width=20, font=("Montserrat", 15))
    entradaDestino.grid(column=1, row=4)

    PedirTicket = Label(window, text="Ticket:", font=("Montserrat", 20, "bold"), fg="#026773")
    PedirTicket.grid(column=0, row=5, padx=(0, 10), pady=15)
    Ticket_entrada = Entry(window, width=20, font=("Montserrat", 15))
    Ticket_entrada.grid(column=1, row=5)

    mensaje_invalido = Label(window, text="", font=("Montserrat", 20), fg="red")
    mensaje_invalido.grid(column=0, row=6, columnspan=2)

    BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
    window.boton_siguiente_imagen = BotonSiguiente
    siguiente = Button(window, image=BotonSiguiente, borderwidth=0, command=lambda: validar_ticket(window, Ticket_entrada, mensaje_invalido))
    siguiente.grid(column=1, row=7, pady=50)

    BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    window.boton_regreso_imagen = BotonRegreso
    regreso = Button(window, image=BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=0, row=7, pady=50)

    def validar_ticket(window, Ticket_entrada, mensaje_invalido):
        ticket = Ticket_entrada.get()
        print(f"Ticket ingresado: {ticket}")

        if len(ticket) == 6:  # El ticket debe tener exactamente 6 caracteres
            mensaje_invalido.config(text="")
            print("Ticket válido. Avanzando a la siguiente pantalla.")
            pantalla_recomendaciones_personal(window, pantalla_personal_datos, pantalla_principal)
        else:
            mensaje_invalido.config(text="Ticket incorrecto")
            print("Ticket inválido. Por favor, ingrese un ticket de 6 caracteres.")

    window.mainloop()