from tkinter import *

window = Tk()
window.title("Personal")
window.minsize(width=800, height=800)

imagen = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Recursos/LogoAeropuerto.png")
imagen.create_image(100,100, image=logo_img)
imagen.grid(column=0, row=0)

tituloPrincipal=Label(text="Personal", font=("Montserrat", 70, "bold"), fg="#011640")
tituloPrincipal.grid(column=1, row=0, columnspan=2)

tituloSecundario=Label(text="Ingresa tu identificacion personal", font=("Montserrat", 20, "bold"), fg="#011640")
tituloSecundario.grid(column=0, row=2, columnspan=2, padx=80)

pedirId=Label(text="ID:", font=("Montserrat", 15, "bold"), fg="#011526")
pedirId.grid(column=0, row=3, sticky="E", pady=20)

idDeEntrada = Entry(width=20, font=("Montserrat", 15))
idDeEntrada.grid(column=1,row=3, sticky="W")

BotonSiguiente = PhotoImage(file="Recursos/BotonSiguiente.png").subsample(2, 2)
siguiente = Button(image=BotonSiguiente, borderwidth=0)
siguiente.grid(column=1, row=10)

BotonRegreso = PhotoImage(file="Recursos/BotonRegreso.png").subsample(2, 2)
siguiente = Button(image=BotonRegreso, borderwidth=0)
siguiente.grid(column=0, row=10)

window.mainloop()