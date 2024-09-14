import tkinter as tk
from tkinter import messagebox

def agregar():
    texto = entrada.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# mostrar datos
lista = tk.Listbox(ventana)
lista.pack(pady=10)

# limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

ventana.mainloop()