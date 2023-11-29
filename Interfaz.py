from tkinter import *
from tkinter import filedialog
import tkinter.ttk as tk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import re
# Importamos la función para limpiar datos
from script_limpieza import limpiar_datos


# Descarga el csv procesado
def descargar_csv(df):
    df.to_csv('db_organizada.csv', index=False)


## Haciendo ventana depuracion csv

def ventana_csv(df, selected_cedula, selected_primer_nombre, selected_segundo_nombre, selected_primer_apellido, selected_segundo_apellido, selected_direccion, selected_telefono, selected_correo):

    # Limpiar la ventana principal (Miventana)
    for widget in Miventana.winfo_children():
        widget.destroy()
    title = tk.Label(Miventana, text="LIMPIANDO DATOS, ESPERE...", font=("Tahoma", 15, "bold"))
    title.pack(ipady=25)

    rename_dict = {}

    # Verificar y agregar al diccionario solo las variables no vacías
    if selected_cedula:
        rename_dict[selected_cedula] = 'cedula'
    if selected_primer_nombre:
        rename_dict[selected_primer_nombre] = 'primer_nombre'
    if selected_segundo_nombre:
        rename_dict[selected_segundo_nombre] = 'segundo_nombre'
    if selected_primer_apellido:
        rename_dict[selected_primer_apellido] = 'primer_apellido'
    if selected_segundo_apellido:
        rename_dict[selected_segundo_apellido] = 'segundo_apellido'
    if selected_direccion:
        rename_dict[selected_direccion] = 'direccion'
    if selected_telefono:
        rename_dict[selected_telefono] = 'telefono'
    if selected_correo:
        rename_dict[selected_correo] = 'correo'

    # Aplicar el renombrado solo si el diccionario no está vacío
    if rename_dict:
        df = df.rename(columns=rename_dict)

    new_df = limpiar_datos(df)

    boton_descargar = Button(Miventana, text="Descargar datos procesados", command=lambda: descargar_csv(new_df))
    boton_descargar.pack()


# Se depuran los datos
def ventana_datos(df, selected_cedula, selected_primer_nombre, selected_segundo_nombre, selected_primer_apellido, selected_segundo_apellido, selected_direccion, selected_telefono, selected_correo):

    # Limpiar la ventana principal (Miventana)
    for widget in Miventana.winfo_children():
        widget.destroy()

    title = tk.Label(Miventana, text="LIMPIANDO DATOS, ESPERE...", font=("Tahoma", 15, "bold"))
    title.pack(ipady=25)

    rename_dict = {}

    # Verificar y agregar al diccionario solo las variables no vacías
    if selected_cedula:
        rename_dict[selected_cedula] = 'cedula'
    if selected_primer_nombre:
        rename_dict[selected_primer_nombre] = 'primer_nombre'
    if selected_segundo_nombre:
        rename_dict[selected_segundo_nombre] = 'segundo_nombre'
    if selected_primer_apellido:
        rename_dict[selected_primer_apellido] = 'primer_apellido'
    if selected_segundo_apellido:
        rename_dict[selected_segundo_apellido] = 'segundo_apellido'
    if selected_direccion:
        rename_dict[selected_direccion] = 'direccion'
    if selected_telefono:
        rename_dict[selected_telefono] = 'telefono'
    if selected_correo:
        rename_dict[selected_correo] = 'correo'

    # Aplicar el renombrado solo si el diccionario no está vacío
    if rename_dict:
        df = df.rename(columns=rename_dict)

    new_df = limpiar_datos(df)

    boton_descargar = Button(Miventana, text="Depurar datos", command=lambda: descargar_csv(new_df))
    boton_descargar.pack()



# Se conecta a base de datos
def nombres_cols(usuario, contrasena, host, db_name, tabla):

    # Limpiar la ventana principal (Miventana)
    for widget in Miventana.winfo_children():
        widget.destroy()

    engine = create_engine('mysql+pymysql://' + usuario + ':'+ contrasena + '@' + host + '/' + db_name)


    consulta_sql = "SELECT * FROM " + tabla

    # Utiliza pandas para leer los datos de la tabla
    df = pd.read_sql_query(consulta_sql, engine)

    # Imprime el DataFrame
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x).replace({'': np.nan})

    columnas = df.columns.tolist()

    # Crear etiquetas y selectores directamente en Miventana
    textos = [
        "Cedula:",
        "Primer nombre:",
        "Segundo nombre:",
        "Primer apellido:",
        "Segundo apellido:",
        "Direccion:",
        "Telefono:",
        "Correo:"
    ]

    opciones = {}

    for i, texto in enumerate(textos):
        frame = Frame(Miventana)
        frame.pack()

        # Etiqueta con el texto específico
        Label(frame, text=texto).pack(side=LEFT)

        # Menú desplegable con nombres de columnas
        opciones[texto] = tk.Combobox(frame, values=columnas)
        opciones[texto].pack(side=LEFT)

    # Función para obtener las opciones seleccionadas
    def obtener_opciones(df):

        # Asignar los valores seleccionados a las variables correspondientes
        selected_cedula = opciones["Cedula:"].get()
        selected_primer_nombre = opciones["Primer nombre:"].get()
        selected_segundo_nombre = opciones["Segundo nombre:"].get()
        selected_primer_apellido = opciones["Primer apellido:"].get()
        selected_segundo_apellido = opciones["Segundo apellido:"].get()
        selected_direccion = opciones["Direccion:"].get()
        selected_telefono = opciones["Telefono:"].get()
        selected_correo = opciones["Correo:"].get()

        # Realizar otras operaciones según sea necesario
        ventana_datos(df, selected_cedula, selected_primer_nombre, selected_segundo_nombre, selected_primer_apellido, selected_segundo_apellido, selected_direccion, selected_telefono, selected_correo)    

    # Botón para obtener las opciones seleccionadas
    boton_obtener = Button(Miventana, text="Depurar datos", command=lambda: obtener_opciones(df))
    boton_obtener.pack()



## Ventana conexion base de datos
def depurar_con_base_de_datos():
    # Limpiar la ventana actual
    for widget in Miventana.winfo_children():
        widget.destroy()

    # Agregar cinco etiquetas y campos de entrada de texto
    label_usuario = Label(Miventana, text="Usuario:")
    label_usuario.pack(pady=10)
    campo_usuario = Entry(Miventana)
    campo_usuario.pack(pady=10)

    label_contrasena = Label(Miventana, text="Contraseña:")
    label_contrasena.pack(pady=10)
    campo_contrasena = Entry(Miventana, show="*")  # Para ocultar la contraseña
    campo_contrasena.pack(pady=10)

    label_host = Label(Miventana, text="Host:")
    label_host.pack(pady=10)
    campo_host = Entry(Miventana)
    campo_host.pack(pady=10)

    label_db_name = Label(Miventana, text="Nombre de la Base de Datos:")
    label_db_name.pack(pady=10)
    campo_db_name = Entry(Miventana)
    campo_db_name.pack(pady=10)

    label_tabla = Label(Miventana, text="Nombre de la Tabla:")
    label_tabla.pack(pady=10)
    campo_tabla = Entry(Miventana)
    campo_tabla.pack(pady=10)

    # Agregar un botón para realizar alguna acción con los campos de texto
    boton_accion = Button(Miventana, text="Obtener datos", command=lambda: nombres_cols(
        campo_usuario.get(), campo_contrasena.get(), campo_host.get(), campo_db_name.get(), campo_tabla.get()
    ))
    boton_accion.pack(pady=10)


## Se busca el archivo
def buscarArchivo():
    archivo_abierto = filedialog.askopenfilename(
        initialdir="/", title="Seleccione archivo", filetypes=(("csv files", "*.csv"), ("all files", "*.*"))
    )
    print(archivo_abierto)
    nArchivo.delete(0, END)  # Limpiar el Entry antes de insertar la nueva ruta
    nArchivo.insert(0, archivo_abierto)
    

## Muestra las columnas del csv
def mostrar_columnas(archivo_csv):
    archivo_csv = nArchivo.get()

    # Limpiar la ventana principal (Miventana)
    for widget in Miventana.winfo_children():
        widget.destroy()
    
    try:
        # Leer las columnas del archivo CSV utilizando pandas
        df = pd.read_csv(archivo_csv, delimiter=";")
        columnas = df.columns.tolist()

        # Crear etiquetas y selectores directamente en Miventana
        textos = [
            "Cedula:",
            "Primer nombre:",
            "Segundo nombre:",
            "Primer apellido:",
            "Segundo apellido:",
            "Direccion:",
            "Telefono:",
            "Correo:"
        ]

        opciones = {}

        for i, texto in enumerate(textos):
            frame = Frame(Miventana)
            frame.pack()

            # Etiqueta con el texto específico
            Label(frame, text=texto).pack(side=LEFT)

            # Menú desplegable con nombres de columnas
            opciones[texto] = tk.Combobox(frame, values=columnas)
            opciones[texto].pack(side=LEFT)

        # Función para obtener las opciones seleccionadas
        def obtener_opciones(df):
            # Asignar los valores seleccionados a las variables correspondientes
            selected_cedula = opciones["Cedula:"].get()
            selected_primer_nombre = opciones["Primer nombre:"].get()
            selected_segundo_nombre = opciones["Segundo nombre:"].get()
            selected_primer_apellido = opciones["Primer apellido:"].get()
            selected_segundo_apellido = opciones["Segundo apellido:"].get()
            selected_direccion = opciones["Direccion:"].get()
            selected_telefono = opciones["Telefono:"].get()
            selected_correo = opciones["Correo:"].get()

            # Realizar otras operaciones según sea necesario
            ventana_csv(df, selected_cedula, selected_primer_nombre, selected_segundo_nombre, selected_primer_apellido, selected_segundo_apellido, selected_direccion, selected_telefono, selected_correo)

        # Botón para obtener las opciones seleccionadas
        boton_obtener = Button(Miventana, text="Depurar datos", command=lambda: obtener_opciones(df))
        boton_obtener.pack()

    except pd.errors.EmptyDataError:
        messagebox.showerror(message="El archivo CSV está vacío o no es válido.")
    except Exception as e:
        messagebox.showerror(message=f"Error al leer el archivo CSV: {str(e)}")



## Subir archivo

def uploadFile():
    archivo_csv = nArchivo.get()
    mostrar_columnas(archivo_csv)

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

botonArchivo = tk.Button(Miventana, text="Buscar archivo CSV", command=buscarArchivo)
botonArchivo.place(relx=0.4, rely=0.6, anchor="center")

botonUpload = tk.Button(Miventana, text="Subir Archivo CSV", command=uploadFile)
botonUpload.place(relx=0.7, rely=0.6, anchor="center")

botonDepurar = tk.Button(Miventana, text="Depurar con Base de Datos", command=depurar_con_base_de_datos)
botonDepurar.place(relx=0.5, rely=0.7, anchor="center")

Miventana.mainloop()
