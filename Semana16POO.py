import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Lista para almacenar las tareas
        self.tasks = []

        # Configuración de estilos
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)
        self.style.map("Treeview", background=[('selected', '#ececec')])

        # Frame para añadir nuevas tareas
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=10, padx=10, fill='x')

        self.entry_task = ttk.Entry(self.frame_input)
        self.entry_task.pack(side='left', fill='x', expand=True, padx=(0, 5))
        self.entry_task.bind("<Return>", self.add_task_event)

        self.btn_add = ttk.Button(self.frame_input, text="Añadir Tarea", command=self.add_task)
        self.btn_add.pack(side='left')

        # Treeview para mostrar las tareas
        self.tree = ttk.Treeview(self.root, columns=("Estado"), show='headings', selectmode='browse')
        self.tree.heading("Estado", text="Tareas")
        self.tree.pack(pady=10, padx=10, fill='both', expand=True)

        # Scrollbar para el Treeview
        self.scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')

        # Botones de acción
        self.frame_buttons = ttk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        self.btn_complete = ttk.Button(self.frame_buttons, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete.grid(row=0, column=0, padx=5)

        self.btn_delete = ttk.Button(self.frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete.grid(row=0, column=1, padx=5)

        # Bindings de teclas
        self.root.bind("<C>", self.complete_task_event)
        self.root.bind("<c>", self.complete_task_event)
        self.root.bind("<Delete>", self.delete_task_event)
        self.root.bind("<D>", self.delete_task_event)
        self.root.bind("<d>", self.delete_task_event)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Inicializar etiquetas para estilos
        self.tree.tag_configure('completed', foreground='gray')
        self.tree.tag_configure('pending', foreground='black')

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task = self.entry_task.get().strip()
        if task == "":
            messagebox.showwarning("Entrada Vacía", "Por favor, introduce una tarea.")
            return
        self.tasks.append({"task": task, "completed": False})
        self.tree.insert('', 'end', values=(task,), tags=('pending',))
        self.entry_task.delete(0, 'end')

    def complete_task_event(self, event):
        self.complete_task()

    def complete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona una tarea para marcar como completada.")
            return
        item = selected_item[0]
        index = self.tree.index(item)
        if not self.tasks[index]["completed"]:
            self.tasks[index]["completed"] = True
            self.tree.item(item, tags=('completed',))
        else:
            # Si ya está completada, la marca como pendiente
            self.tasks[index]["completed"] = False
            self.tree.item(item, tags=('pending',))

    def delete_task_event(self, event):
        self.delete_task()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona una tarea para eliminar.")
            return
        item = selected_item[0]
        index = self.tree.index(item)
        del self.tasks[index]
        self.tree.delete(item)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
