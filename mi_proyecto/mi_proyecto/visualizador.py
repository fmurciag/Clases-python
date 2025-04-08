import os
import tkinter as tk
from tkinter import filedialog, Text


class VisualizadorArchivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Archivos")
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=1, fill="both")
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Salir", command=self.root.quit)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                contenido = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contenido)


if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizadorArchivos(root)
    root.mainloop()
