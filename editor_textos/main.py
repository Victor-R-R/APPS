import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto")

        # Crear el cuadro de texto
        self.text = tk.Text(self.master)
        self.text.pack(expand=True, fill="both")

        # Crear el menú de opciones
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abir", command=self.open_file)
        filemenu.add_command(label="Guardar", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.master.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.master.config(menu=menubar)

        # Variables de instancia para el archivo abierto y su contenido
        self.filename = None
        self.filecontent = None

    def open_file(self):
        # Abrir un diálogo para seleccionar el archivo
        self.filename = filedialog.askopenfilename(initialdir='.', title="Seleccionar archivo",
                                                   filetypes=(
                                                    ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))
        

        # Leer el contenido del archivo seleccionado y mostrarlo en el cuadro de texto  
        with open(self.filename, "r") as f:
            self.filecontent = f.read()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, self.filecontent)

    def save_file(self):
        # Si no hay archivo abierto, abrir un diálogo para seleccionar la ubicación
        if self.filename is None:
            self.filename = filedialog.asksaveasfilename(initialdir=".", title="Guardar",
                                                       defaultextension=".txt", filetypes=(
                ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))
            if not self.filename:
                return
            
        # Guardar el contenido actual del cuadro de texto en el archivo seleccionado
        self.filecontent = self.text.get("1.0", tk.END)
        with open(self.filename, "w") as f:
            f.write(self.filecontent)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()