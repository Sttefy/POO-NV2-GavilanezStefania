import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Crear los Frames principales
        self.create_frames()

        # Crear los componentes dentro de los Frames
        self.create_treeview()
        self.create_input_fields()
        self.create_buttons()

    def create_frames(self):
        # Frame para la visualización de eventos
        self.frame_display = ttk.Frame(self.root)
        self.frame_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Frame para la entrada de datos
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(padx=10, pady=5, fill=tk.X)

        # Frame para los botones de acción
        self.frame_buttons = ttk.Frame(self.root)
        self.frame_buttons.pack(padx=10, pady=10, fill=tk.X)

    def create_treeview(self):
        # Definir columnas
        columns = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(self.frame_display, columns=columns, show='headings')

        # Definir encabezados
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.CENTER)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_display, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def create_input_fields(self):
        # Etiquetas y campos de entrada
        lbl_fecha = ttk.Label(self.frame_input, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_fecha = DateEntry(self.frame_input, width=12, background='darkblue',
                                     foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        lbl_hora = ttk.Label(self.frame_input, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        self.entry_hora = ttk.Entry(self.frame_input, width=10)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        lbl_descripcion = ttk.Label(self.frame_input, text="Descripción:")
        lbl_descripcion.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.entry_descripcion = ttk.Entry(self.frame_input, width=50)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)

    def create_buttons(self):
        # Botón para agregar evento
        btn_agregar = ttk.Button(self.frame_buttons, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar evento seleccionado
        btn_eliminar = ttk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir de la aplicación
        btn_salir = ttk.Button(self.frame_buttons, text="Salir", command=self.root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        # Validar campos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        # Validar formato de hora
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato de Hora Inválido", "La hora debe tener el formato HH:MM.")
            return

        # Insertar en Treeview
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona un evento para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirm:
            for item in selected_item:
                self.tree.delete(item)

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
