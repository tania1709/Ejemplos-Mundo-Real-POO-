import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(self.root, width=40)
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas
        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def complete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            task = self.tasks[task_index]
            self.tasks[task_index] = f"[COMPLETADA] {task}"
            self.listbox.delete(task_index)
            self.listbox.insert(task_index, self.tasks[task_index])
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para marcar como completada")

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.listbox.delete(task_index)
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()