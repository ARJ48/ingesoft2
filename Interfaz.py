from tkinter import *
from tkinter import filedialog
import tkinter.ttk as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import pandas as pd

import csv

def buscarArchivo():
    archivo_abierto = filedialog.askopenfilename(
        initialdir="/", title="Seleccione archivo", filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
    )
    print(archivo_abierto)
    nArchivo.delete(0, END)  # Limpiar el Entry antes de insertar la nueva ruta
    nArchivo.insert(0, archivo_abierto)
    
selected_cedula = ""
selected_primer_nombre = ""
selected_segundo_nombre = ""
selected_primer_apellido = ""
selected_segundo_apellido = ""
selected_direccion = ""
selected_telefono = ""
selected_correo = ""

def mostrar_columnas(archivo_csv):
    try:
        # Leer las columnas del archivo CSV utilizando pandas
        df = pd.read_csv(archivo_csv)
        columnas = str(df.columns.tolist()).split(";")

        # Crear una nueva ventana para mostrar etiquetas y selectores
        ventana_selectores = Toplevel(Miventana)
        ventana_selectores.title("Selectores de Columnas")

        # Crear etiquetas y selectores
        textos = [
            "Cedula",
            "Primer_nombre",
            "Segundo_nombre",
            "Primer_apellido",
            "Segundo_apellido",
            "Direccion",
            "Telefono",
            "Correo"
        ]

        opciones = {}

        for i, texto in enumerate(textos):
            frame = Frame(ventana_selectores)
            frame.pack()

            # Etiqueta con el texto específico
            Label(frame, text=texto).pack(side=LEFT)

            # Menú desplegable con nombres de columnas
            opciones[texto] = tk.Combobox(frame, values=columnas)
            opciones[texto].pack(side=LEFT)

        # Función para obtener las opciones seleccionadas
        def obtener_opciones():
            # Usar la palabra clave global para acceder a variables globales
            global selected_cedula, selected_primer_nombre, selected_segundo_nombre
            global selected_primer_apellido, selected_segundo_apellido, selected_direccion
            global selected_telefono, selected_correo

            # Asignar los valores seleccionados a las variables correspondientes
            selected_cedula = opciones["Cedula"].get()
            selected_primer_nombre = opciones["Primer_nombre"].get()
            selected_segundo_nombre = opciones["Segundo_nombre"].get()
            selected_primer_apellido = opciones["Primer_apellido"].get()
            selected_segundo_apellido = opciones["Segundo_apellido"].get()
            selected_direccion = opciones["Direccion"].get()
            selected_telefono = opciones["Telefono"].get()
            selected_correo = opciones["Correo"].get()

            print("Opciones obtenidas:")
            print(f"Cedula: {selected_cedula}")
            print(f"Primer_nombre: {selected_primer_nombre}")
            print(f"Segundo_nombre: {selected_segundo_nombre}")
            print(f"Primer_apellido: {selected_primer_apellido}")
            print(f"Segundo_apellido: {selected_segundo_apellido}")
            print(f"Direccion: {selected_direccion}")
            print(f"Telefono: {selected_telefono}")
            print(f"Correo: {selected_correo}")

        # Botón para obtener las opciones seleccionadas
        boton_obtener = Button(ventana_selectores, text="Obtener Opciones", command=obtener_opciones)
        boton_obtener.pack()


    except pd.errors.EmptyDataError:
        messagebox.showerror(message="El archivo CSV está vacío o no es válido.")
    except Exception as e:
        messagebox.showerror(message=f"Error al leer el archivo CSV: {str(e)}")

def uploadFile():
    if len(nArchivo.get()) == 0:
        messagebox.showerror(message="DEBE DE SELECCIONAR UNA UBICACIÓN VÁLIDA.")
    else:
        archivo_csv = nArchivo.get()
        mostrar_columnas(archivo_csv)
        messagebox.showinfo(message="Archivo cargado satisfactoriamente")

Miventana = Tk()
Miventana.geometry("500x500")
Miventana.title("PROYECTO FINAL")
Miventana.resizable(0, 0)

style = ThemedStyle(Miventana)
style.set_theme("arc")

title = tk.Label(Miventana, text="PROYECTO INGESOFT II - TOTAL REPORT", font=("Tahoma", 15, "bold"))
title.pack(ipady=25)

nArchivo = tk.Entry(Miventana, width=70)
nArchivo.place(relx=0.5, rely=0.5, anchor="center")

botonArchivo = tk.Button(Miventana, text="Examinar", command=buscarArchivo)
botonArchivo.place(relx=0.4, rely=0.6, anchor="center")

botonUpload = tk.Button(Miventana, text="Subir Archivo", command=uploadFile)
botonUpload.place(relx=0.6, rely=0.6, anchor="center")

Miventana.mainloop()
