import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, texto):
        self.texto = texto
        self.completada = False

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x300")
        self.tareas = []
        self.lista_tareas = tk.Listbox(self.root)
        self.lista_tareas.pack(padx=10, pady=10)
        self.entry_tarea = tk.Entry(self.root)
        self.entry_tarea.pack(padx=10, pady=10)
        self.button_anadir = tk.Button(self.root, text="Añadir", command=self.anadir_tarea)
        self.button_anadir.pack(padx=10, pady=10)
        self.button_completar = tk.Button(self.root, text="Completar", command=self.completar_tarea)
        self.button_completar.pack(padx=10, pady=10)
        self.button_eliminar = tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea)
        self.button_eliminar.pack(padx=10, pady=10)
        self.root.bind("<Return>", self.anadir_tarea_con_enter)
        self.root.bind("<c>", self.completar_tarea_con_c)
        self.root.bind("<Delete>", self.eliminar_tarea_con_delete)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def anadir_tarea(self):
        texto = self.entry_tarea.get()
        if texto:
            tarea = Tarea(texto)
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, texto)
            self.entry_tarea.delete(0, tk.END)

    def anadir_tarea_con_enter(self, event):
        self.anadir_tarea()

    def completar_tarea(self):
        indice = self.lista_tareas.curselection()
        if indice:
            tarea = self.tareas[indice[0]]
            tarea.completada = True
            self.lista_tareas.itemconfig(indice, fg="green")

    def completar_tarea_con_c(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        indice = self.lista_tareas.curselection()
        if indice:
            self.tareas.pop(indice[0])
            self.lista_tareas.delete(indice)

    def eliminar_tarea_con_delete(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()