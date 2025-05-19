import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from  analisis import DataAnalyzer
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import simpledialog, filedialog
from PIL import ImageTk

data=pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)
info =analizar.summary()

def informacion():
    try:
        text_area.delete("1.0", tk.END)
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("Error", "No se puede")

def mostrar_imagenes(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    image_label.configure(image=image_tk)
    image_label.image = image_tk

def mostrar_correlacion():
    img = analizar.correlation_matrix()
    mostrar_imagenes(img)

def mostrar_categorico():
    cols = analizar.df.select_dtypes(include="object").columns.to_list()
    if not cols:
        messagebox.showwarning("Atención", "El DataFrame no tiene una col. categóricas")
    else:
        sel = simpledialog.askstring("Columna", f"Elige una: \n {cols}")
        if sel in cols:
            img = analizar.categorical_analisis_col(sel)
            mostrar_imagenes(img)


ventana = tk.Tk()

ventana.title("Análisis de datos")
ventana.geometry("600x1000")

boton_summary = tk.Button(ventana, text="Estadísticas", command= informacion)
boton_summary.grid(row=1, column=0)

boton_numérico = tk.Button(ventana, text="Mostrar correlación", command= mostrar_correlacion)
boton_numérico.grid(row=0, column=1)

boton_categorico = tk.Button(ventana, text="Categórico", command= informacion)
boton_categorico.grid(row=1, column=2)

text_area = ScrolledText(ventana, width= 70, height=30)
text_area.grid(row=1, column=1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)
image_label = tk.Label(content_frame, text= "Resultado")
image_label.grid(row=0, column=0)


ventana.mainloop()