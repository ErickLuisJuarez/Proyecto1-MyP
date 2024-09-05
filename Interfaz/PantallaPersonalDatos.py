from tkinter import *

from tkinter import *

def pantalla_personal_datos(window, pantalla_principal):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("Personal")
    #window.minsize(width=800, height=800)
    window.config(padx=20, pady=20)

    imagen = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="Recursos/LogoAeropuerto.png")
    imagen.create_image(100,100, image=logo_img)
    imagen.grid(column=0, row=0)

    tituloPrincipal=Label(text="Personal", font=("Montserrat", 60, "bold"), fg="#011640")
    tituloPrincipal.grid(column=1, row=0, pady=20, sticky="w")

    tituloSecundario=Label(text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
    tituloSecundario.grid(column=0, row=1, columnspan=3, padx=150, sticky="n", pady=15)

    Origen=Label(text="Origen", font=("Montserrat", 20, "bold"), fg="#026773")
    Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
    entradaOrigen = Entry(width= 20, font=("Montserrat", 15))
    entradaOrigen.grid(column=1, row=3)

    Destino=Label(text="Destino", font=("Montserrat", 20, "bold"), fg="#026773")
    Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
    entradaDestino = Entry(width= 20, font=("Montserrat", 15))
    entradaDestino.grid(column=1, row=4)

    HoraDeSalida=Label(text="Hora de salida", font=("Montserrat", 20, "bold"), fg="#026773")
    HoraDeSalida.grid(column=0, row=5, padx=(0, 10), pady=15)
    entradaHoraSalida = Entry(width= 20, font=("Montserrat", 15))
    entradaHoraSalida.grid(column=1, row=5)

    HoraDellegada=Label(text="Hora de llegada", font=("Montserrat", 20, "bold"), fg="#026773")
    HoraDellegada.grid(column=0, row=6, padx=(0, 10), pady=15)
    entradaHoraLlegada = Entry(width= 20, font=("Montserrat", 15))
    entradaHoraLlegada.grid(column=1, row=6)

    PedirTicket=Label(text="Ticket:", font=("Montserrat", 20, "bold"), fg="#026773")
    PedirTicket.grid(column=0, row=7, padx=(0, 10), pady=15)
    input = Entry(width= 20, font=("Montserrat", 15))
    input.grid(column=1, row=7)

    window.BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
    siguiente = Button(window, image=window.BotonSiguiente, borderwidth=0)
    siguiente.grid(column=1, row=10)

    window.BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
    regreso = Button(window, image=window.BotonRegreso, borderwidth=0, command=lambda: pantalla_principal(window))
    regreso.grid(column=0, row=10)

    #window.mainloop()