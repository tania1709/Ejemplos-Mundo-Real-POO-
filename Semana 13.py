
import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación GUI Básica")

        # Etiqueta y campo de texto para ingresar información
        self.etiqueta = tk.Label(self.ventana, text="Ingrese información:")
        self.etiqueta.pack()
        self.campo_texto = tk.Entry(self.ventana)
        self.campo_texto.pack()

        # Botón para agregar información
        self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_informacion)
        self.boton_agregar.pack()

        # Lista para mostrar información
        self.lista = tk.Listbox(self.ventana)
        self.lista.pack()

        # Botón para limpiar información
        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar_informacion)
        self.boton_limpiar.pack()

    def agregar_informacion(self):
        informacion = self.campo_texto.get()
        if informacion:
            self.lista.insert(tk.END, informacion)
            self.campo_texto.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Ingrese información válida")

    def limpiar_informacion(self):
        self.lista.delete(0, tk.END)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    aplicacion = AplicacionGUI()
    aplicacion.run()