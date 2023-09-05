import json
import tkinter as tk
from tkinter import ttk

# Función para leer el archivo JSON
def leer_archivo():
    with open('lector_ficheros_json/productos.json') as archivo:
        productos = json.load(archivo)
    return productos

# Función para crear la tabla con los datos de los productos
def crear_tabla():
    # Crear la tabla
    tabla = ttk.Treeview(ventana)
    tabla['columns'] = ('ID', 'NOMBRE', 'DESCRIPCION', 'PRECIO')
    tabla.column('#0', width=0, stretch=tk.NO)
    tabla.column('ID', anchor=tk.CENTER, width=50)
    tabla.column('NOMBRE', anchor=tk.CENTER, width=150)
    tabla.column('DESCRIPCION', anchor=tk.CENTER, width=250)
    tabla.column('PRECIO', anchor=tk.CENTER, width=80)

    # Crear los encabezados de la tabla
    tabla.heading('#0', text='', anchor=tk.CENTER)
    tabla.heading('ID', text='ID', anchor=tk.CENTER)
    tabla.heading('NOMBRE', text='NOMBRE', anchor=tk.CENTER)
    tabla.heading('DESCRIPCION', text='DESCRIPCION', anchor=tk.CENTER)
    tabla.heading('PRECIO', text='PRECIO', anchor=tk.CENTER)

    # Agregar los datos de los productos a la tabla
    productos = leer_archivo()
    for producto in productos:
        tabla.insert(parent='', index='end', iid=producto['ID'], text='',
                     values=(producto['ID'], producto['NOMBRE'], producto['DESCRIPCION'], f"{producto['PRECIO']:.2F}€"))
        
    # Función para mostrar la información de un producto en una tabla emergente
    def mostrar_producto(event):
        # Obtener el índice del producto seleccionado
        item_id = tabla.focus()

        # Obtener los datos del producto seleccionado
        producto = [value for value in tabla.item(item_id)['values']]

        # Crear la ventana emergente
        ventana_producto = tk.Toplevel(ventana)
        ventana_producto.title(f'Producto {producto[0]}')
        ventana_producto.geometry('300x200')   

        # Crear las etiquetas para mostar los datos del producto
        lbl_nombre = tk.Label(ventana_producto, text=f'Nombre: {producto[1]}', font=('Arial', 12))
        lbl_nombre.pack(pady=10)
        lbl_desripcion = tk.Label(ventana_producto, text=f'Descripción: {producto[2]}', font=('Arial', 12))
        lbl_desripcion.pack(pady=10)
        lbl_nombre = tk.Label(ventana_producto, text=f'Nombre: {producto[3]}', font=('Arial', 12))
        lbl_nombre.pack(pady=10)

    # Asignar la función de mostrar el producto al evento de doble clic en la tabla
    tabla.bind('<Double-Button-1>', mostrar_producto)

    return tabla

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Lista de Productos')
ventana.geometry('550x400')

# Crear la tabla y mostrarla en la ventana
tabla = crear_tabla()
tabla.pack(fill='both', expand=True)

# Iniciar la aplicación
ventana.mainloop()
