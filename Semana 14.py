import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear contenedores
        self.frame_events = tk.Frame(self.root)
        self.frame_events.pack(fill="both", expand=True)

        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack(fill="x")

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(fill="x")

        # Crear lista de eventos
        self.tree_events = ttk.Treeview(self.frame_events)
        self.tree_events["columns"] = ("Fecha", "Hora", "Descripción")
        self.tree_events.column("#0", width=0, stretch=tk.NO)
        self.tree_events.column("Fecha", anchor=tk.W, width=100)
        self.tree_events.column("Hora", anchor=tk.W, width=100)
        self.tree_events.column("Descripción", anchor=tk.W, width=200)
        self.tree_events.heading("#0", text="", anchor=tk.W)
        self.tree_events.heading("Fecha", text="Fecha", anchor=tk.W)
        self.tree_events.heading("Hora", text="Hora", anchor=tk.W)
        self.tree_events.heading("Descripción", text="Descripción", anchor=tk.W)
        self.tree_events.pack(fill="both", expand=True)

        # Crear campos de entrada
        self.label_date = tk.Label(self.frame_input, text="Fecha (dd/mm/aaaa):")
        self.label_date.pack(side=tk.LEFT)
        self.entry_date = tk.Entry(self.frame_input)
        self.entry_date.pack(side=tk.LEFT)

        self.label_time = tk.Label(self.frame_input, text="Hora (hh:mm):")
        self.label_time.pack(side=tk.LEFT)
        self.entry_time = tk.Entry(self.frame_input)
        self.entry_time.pack(side=tk.LEFT)

        self.label_description = tk.Label(self.frame_input, text="Descripción:")
        self.label_description.pack(side=tk.LEFT)
        self.entry_description = tk.Entry(self.frame_input)
        self.entry_description.pack(side=tk.LEFT)

        # Crear botones
        self.button_add = tk.Button(self.frame_buttons, text="Agregar Evento", command=self.add_event)
        self.button_add.pack(side=tk.LEFT)

        self.button_delete = tk.Button(self.frame_buttons, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.button_delete.pack(side=tk.LEFT)

        self.button_exit = tk.Button(self.frame_buttons, text="Salir", command=self.root.destroy)
        self.button_exit.pack(side=tk.LEFT)

    def add_event(self):
        date = self.entry_date.get()
        time = self.entry_time.get()
        description = self.entry_description.get()
        # Validar fecha y hora
        try:
            datetime.strptime(date, "%d/%m/%Y")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Fecha o hora inválida")
            return
        # Agregar evento
        self.tree_events.insert("", "end", values=(date, time, description))
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.tree_events.selection()
        if selected_item:
            self.tree_events.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "No hay evento seleccionado")

if __name__ == "__main__":
    root = tk.Tk()
    agenda = AgendaPersonal(root)
    root.mainloop()
