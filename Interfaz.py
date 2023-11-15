from tkinter import *
from tkinter import filedialog
import tkinter.ttk as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle


def buscarArchivo():
    archivo_abierto = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo", filetypes=(("csv files", "*.csv"),
                                                                                                       ("all files", "*.*")))
    print(archivo_abierto)
    nArchivo.delete(0, END)  # Limpiar el Entry antes de insertar la nueva ruta
    nArchivo.insert(0, archivo_abierto)

def uploadFile():
    if len(nArchivo.get()) == 0:
        messagebox.showerror(message="DEBE DE SELECCIONAR UNA UBICACIÓN VÁLIDA.")
    else:
        barraP= tk.Progressbar(Miventana,mode="determinate")
        barraP.place(relx=0.5, rely=0.8, anchor="center")
        def progreso():
            actual= barraP["value"]
            nuevo= actual+10
            barraP["value"]= nuevo
            if nuevo < 100:
                Miventana.after(500, progreso)
            else:
                messagebox.showinfo(message="Archivo cargado satisfactoriamente")
                Miventana.destroy() 
                return
        progreso()
        
Miventana= Tk()
Miventana.geometry("500x500")
Miventana.title("PROYECTO FINAL")
Miventana.resizable(0, 0)

style= ThemedStyle(Miventana)
style.set_theme("arc")

title= tk.Label(Miventana, text="PROYECTO INGESOFT II - TOTAL REPORT", font=("Tahoma", 15, "bold"))
title.pack(ipady=25)

nArchivo= tk.Entry(Miventana, width=70)  
nArchivo.place(relx=0.5, rely=0.5, anchor="center")

botonArchivo= tk.Button(Miventana, text="Examinar", command=buscarArchivo)
botonArchivo.place(relx=0.4, rely=0.6, anchor="center")

botonUpload= tk.Button(Miventana, text="Subir Archivo", command=uploadFile)
botonUpload.place(relx=0.6, rely=0.6, anchor="center")
Miventana.mainloop()
