import tkinter as tk

def mostrar_nueva_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.transient(root)
    nueva_ventana.title("Nueva Ventana")
    
    etiqueta_nuevo_contenido = tk.Label(nueva_ventana, text="¡Hola! Este es el nuevo contenido.")
    etiqueta_nuevo_contenido.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("500x500")

# Crear un botón que muestra una nueva ventana con contenido al hacer clic
boton_mostrar_nueva_ventana = tk.Button(root, text="Mostrar Nueva Ventana", command=mostrar_nueva_ventana)
boton_mostrar_nueva_ventana.pack()

# Iniciar el bucle principal
root.mainloop()
