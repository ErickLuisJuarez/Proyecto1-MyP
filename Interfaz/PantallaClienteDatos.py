from tkinter import *

window = Tk()
window.title("Cliente")
window.minsize(width=800, height=800)
window.config(padx=20, pady=20)

lienzo = Canvas(width=200, height=200)
logoaeropuerto = PhotoImage(file="/home/tomas/Documentos/Modelado/borrador1/LogoAeropuerto.png")
lienzo.create_image(100, 100, image=logoaeropuerto)
lienzo.grid(column=0, row=0, padx=(0, 10))

titulo1=Label(text="Cliente", font=("Montserrat", 60, "bold"), fg="#011640")
titulo1.grid(column=1, row=0, pady=20, sticky="w")

titulo2=Label(text="Rellene los siguientes datos", font=("Montserrat", 25, "bold"), fg="#3CA6A6")
titulo2.grid(column=0, row=1, columnspan=3, padx=150, sticky="n", pady=15)

Origen=Label(text="Origen", font=("Montserrat", 20, "bold"), fg="#026773")
Origen.grid(column=0, row=3, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=3)

Destino=Label(text="Destino", font=("Montserrat", 20, "bold"), fg="#026773")
Destino.grid(column=0, row=4, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=4)

HoradeSalida=Label(text="Hora de salida", font=("Montserrat", 20, "bold"), fg="#026773")
HoradeSalida.grid(column=0, row=5, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=5)

Horadellegada=Label(text="Hora de llegada", font=("Montserrat", 20, "bold"), fg="#026773")
Horadellegada.grid(column=0, row=6, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=6)

LatitudOrigen=Label(text="Latitud del origen", font=("Montserrat", 20, "bold"), fg="#026773")
LatitudOrigen.grid(column=0, row=7, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=7)

LatitudDestino=Label(text="Latitud del destino", font=("Montserrat", 20, "bold"), fg="#026773")
LatitudDestino.grid(column=0, row=8, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=8)

LongitudDestino=Label(text="Longitud del destino", font=("Montserrat", 20, "bold"), fg="#026773")
LongitudDestino.grid(column=0, row=9, padx=(0, 10), pady=15)
input = Entry(width= 20, font=("Montserrat", 15))
input.grid(column=1, row=9)

window.mainloop()