import tkinter as tk
from tkinter import ttk, messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Lista para almacenar las tareas
        self.tasks = []

        # Configurar el estilo
        self.configure_style()

        # Crear los componentes de la interfaz
        self.create_widgets()

    def configure_style(self):
        style = ttk.Style()
        style.configure("TButton", padding=6)
        style.configure("TLabel", padding=6)
        style.configure("TEntry", padding=6)
        # Estilo para tareas completadas
        style.configure("Completed.TLabel", foreground="gray", font=("Arial", 10, "overstrike"))

    def create_widgets(self):
        # Frame para la entrada de tareas
        frame_input = ttk.Frame(self.root)
        frame_input.pack(padx=10, pady=10, fill=tk.X)

        lbl_task = ttk.Label(frame_input, text="Nueva Tarea:")
        lbl_task.pack(side=tk.LEFT, padx=(0, 5))

        self.entry_task = ttk.Entry(frame_input)
        self.entry_task.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_task.bind("<Return>", self.add_task_event)  # Manejador para la tecla Enter

        btn_add = ttk.Button(frame_input, text="Añadir Tarea", command=self.add_task)
        btn_add.pack(side=tk.LEFT, padx=(5, 0))

        # Frame para la lista de tareas
        frame_list = ttk.Frame(self.root)
        frame_list.pack(padx=10, pady=(0,10), fill=tk.BOTH, expand=True)

        self.listbox_tasks = tk.Listbox(frame_list, selectmode=tk.SINGLE, font=("Arial", 12))
        self.listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox_tasks.bind("<Double-1>", self.toggle_task_completion)  # Manejador para doble clic

        scrollbar = ttk.Scrollbar(frame_list, orient=tk.VERTICAL, command=self.listbox_tasks.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_tasks.config(yscrollcommand=scrollbar.set)

        # Frame para los botones de acción
        frame_buttons = ttk.Frame(self.root)
        frame_buttons.pack(padx=10, pady=10, fill=tk.X)

        btn_complete = ttk.Button(frame_buttons, text="Marcar como Completada", command=self.complete_task)
        btn_complete.pack(side=tk.LEFT, padx=(0,5))

        btn_delete = ttk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.pack(side=tk.LEFT, padx=(5,0))

    def add_task_event(self, event):
        """Manejador de evento para añadir tarea al presionar Enter."""
        self.add_task()

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.entry_task.get().strip()
        if task == "":
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa una tarea.")
            return
        self.tasks.append({"description": task, "completed": False})
        self.update_task_list()
        self.entry_task.delete(0, tk.END)

    def update_task_list(self):
        """Actualiza la visualización de la lista de tareas."""
        self.listbox_tasks.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            display_text = task["description"]
            if task["completed"]:
                display_text = f"✔ {display_text}"
                self.listbox_tasks.insert(tk.END, display_text)
                self.listbox_tasks.itemconfig(index, {'fg': 'gray'})
            else:
                self.listbox_tasks.insert(tk.END, display_text)

    def complete_task(self):
        """Marca la tarea seleccionada como completada."""
        selected_index = self.listbox_tasks.curselection()
        if not selected_index:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona una tarea para marcar como completada.")
            return
        index = selected_index[0]
        if not self.tasks[index]["completed"]:
            self.tasks[index]["completed"] = True
            self.update_task_list()
        else:
            messagebox.showinfo("Tarea Ya Completada", "La tarea seleccionada ya está marcada como completada.")

    def toggle_task_completion(self, event):
        """Alterna el estado de completado de una tarea al hacer doble clic."""
        selected_index = self.listbox_tasks.curselection()
        if not selected_index:
            return
        index = selected_index[0]
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.update_task_list()

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_index = self.listbox_tasks.curselection()
        if not selected_index:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona una tarea para eliminar.")
            return
        index = selected_index[0]
        task_description = self.tasks[index]["description"]
        confirm = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar la tarea:\n\n'{task_description}'?")
        if confirm:
            del self.tasks[index]
            self.update_task_list()

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
