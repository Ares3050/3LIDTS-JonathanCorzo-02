import tkinter as ttk


ventana = ttk.Tk()
ventana.title("Practica 02 py")
ventana.geometry("520x480")
LbNombre = ttk.Label(ventana,text="Ingrese nombre :")
LbNombre.place
LbNombre.place(x=120,y=100)
tbNombre = ttk.Entry()
tbNombre.place(x=120,y=100, width=200)
btnAceptar = ttk.Button(text="Aceptar")
btnAceptar.place(x=120, y=140)
btnCancelar = ttk.Button(text="Cancelar")
btnCancelar.place(x=280, y=200)
ventana.mainloop()
