from tkinter import *
from PantallaRecomendacionesCliente import pantalla_recomendaciones_cliente

def pantalla_cliente(window, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()
    
    window.title("Cliente")

    window.geometry("1200x500")
    window.minsize(width=800, height=800)
    window.config(padx=20, pady=20)

    lienzo = Canvas(window, width=200, height=200)
    logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
    lienzo.create_image(100, 100, image=logoaeropuerto)
    lienzo.grid(column=0, row=0, padx=(0, 10))

    titulo1 = Label(window, text="Cliente", font=("Montserrat", 60, "bold"), fg="#011640")
    titulo1.grid(column=1, row=0, pady=20, sticky="w")

    titulo2 = Label(window, text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
    titulo2.grid(column=0, row=1, columnspan=3, padx=150, pady=50, sticky="n")

    Origen = Label(window, text="Origen:", font=("Montserrat", 20, "bold"), fg="#026773")
    Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
    entradaOrigen = Entry(window, width=20, font=("Montserrat", 15))
    entradaOrigen.grid(column=1, row=3)

    Destino = Label(window, text="Destino:", font=("Montserrat", 20, "bold"), fg="#026773")
    Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
    entradaDestino = Entry(window, width=20, font=("Montserrat", 15))
    entradaDestino.grid(column=1, row=4)

    Pedir_ticket = Label(window, text="Ticket:", font=("Montserrat", 20, "bold"), fg="#026773")
    Pedir_ticket.grid(column=0, row=5, padx=(0, 10), pady=15)
    Ticket_entrada = Entry(window, width=20, font=("Montserrat", 15, "bold"))
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
            pantalla_recomendaciones_cliente(window, pantalla_cliente, pantalla_principal)
        else:
            mensaje_invalido.config(text="Ticket incorrecto")
            print("Ticket inválido. Por favor, ingrese un ticket de 6 caracteres.")  

    window.mainloop()