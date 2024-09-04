from tkinter import *

window = Tk()
window.title("Cliente")
window.minsize(width=800, height=800)
window.config(padx=20, pady=20)

lienzo = Canvas(width=200, height=200)
logoaeropuerto = PhotoImage(file="Recursos/LogoAeropuerto.png")
lienzo.create_image(100, 100, image=logoaeropuerto)
lienzo.grid(column=0, row=0, padx=(0, 10))

titulo1=Label(text="Cliente", font=("Montserrat", 60, "bold"), fg="#011640")
titulo1.grid(column=1, row=0, sticky="w")

titulo2=Label(text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
titulo2.grid(column=0, row=1, columnspan=3, padx=150, sticky="n")

Origen=Label(text="Origen:", font=("Montserrat", 20, "bold"), fg="#026773")
Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=3)

Destino=Label(text="Destino:", font=("Montserrat", 20, "bold"), fg="#026773")
Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=4)

HoradeSalida=Label(text="Hora de salida:", font=("Montserrat", 20, "bold"), fg="#026773")
HoradeSalida.grid(column=0, row=5, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=5)

Horadellegada=Label(text="Hora de llegada:", font=("Montserrat", 20, "bold"), fg="#026773")
Horadellegada.grid(column=0, row=6, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=6)

LatitudOrigen=Label(text="Ticket:", font=("Montserrat", 20, "bold"), fg="#026773")
LatitudOrigen.grid(column=0, row=7, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=7)

BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
siguiente = Button(image=BotonSiguiente, borderwidth=0)
siguiente.grid(column=1, row=10)

BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
siguiente = Button(image=BotonRegreso, borderwidth=0)
siguiente.grid(column=0, row=10)
window.mainloop()