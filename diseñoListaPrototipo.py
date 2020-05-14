import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from json import *
import requests #Importando requests


'''RECUERDEN COMENTAR SUS CAMBIOS'''

screenSize = {'width': 360, 'height': 800}
root = tk.Tk()
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)


class app:
    def __init__(self, master, titulo):
        self.screen = tk.Frame(master)
        self.screen.place(height=800, width=360, anchor=tk.NW)
        self.titulo = titulo
        root.title(self.titulo)
        self.encabezado = tk.Frame(self.screen, bg="lime green")
        self.encabezado.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
        self.encabezado.place_configure(relx=0, rely=0)

        self.label_titulo = tk.Label(self.encabezado,
                                     bg="lime green",
                                     fg="white",
                                     text=self.titulo,
                                     font=tkFont.Font(family='Roboto', size=20)
                                     )
        self.label_titulo.place(anchor=tk.NW, relx=0.1, rely=0.2)

        self.cuerpo = tk.Frame(self.screen, bg="white")
        self.cuerpo.place(anchor=tk.NW, relwidth=1.0,
                          relheight=0.9, relx=0, rely=0.1)


class meme(app): ##AGREGUE EL FORMATO PARA LA VENTANA DONDE MUESTRA EL MEME
    def __init__(self, master, titulo, descripcion_meme):
        super().__init__(master, titulo)
        self.screen = tk.Frame(master)
        self.screen.place(height=800, width=360, anchor=tk.NW)
        self.titulo = titulo
        root.title(self.titulo)
        self.encabezado = tk.Frame(self.screen, bg="lime green")
        self.encabezado.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
        self.encabezado.place_configure(relx=0, rely=0)

        self.label_titulo = tk.Label(self.encabezado,
                                     bg="lime green",
                                     fg="white",
                                     text=titulo,
                                     font=tkFont.Font(family='Roboto', size=13)
                                     )
        self.label_titulo.place(anchor=tk.NW, relx=0.1, rely=0.2)

        self.cuerpo = tk.Frame(self.screen, bg="white")
        self.cuerpo.place(anchor=tk.NW, relwidth=1.0,
                          relheight=0.9, relx=0, rely=0.1)
        self.canvas = tk.Canvas(self.cuerpo, bg = "black", width = 300,height = 300)
        self.canvas.place(anchor = tk.NW,relx = 0.075, rely = 0.15)
        self.Descripcion = tk.Message(self.cuerpo,
                                     bg = 'white', 
                                     text = descripcion_meme,
                                     font=tkFont.Font(family='Roboto', size=15)
                                     )
        self.Descripcion.place(anchor = tk.NW, relx = 0.1, rely = 0.6)
        self.Regresar = tk.Button(self.cuerpo,
                                 bg = 'white', 
                                 text = 'Regresar',
                                 font=tkFont.Font(family='Roboto', size=15)
                                 )
        self.Regresar.place(anchor = tk.NW, relx = 0.4, rely = 0.9)

class lista(app):
    def __init__(self, master, titulo):
        super().__init__(master, titulo)


lista_memes = lista(root, 'LISTA DE MEMES')
##Aqui forma la ventana del meme
vista_memes = meme(root,'AQUI VA EL TITULO DEL MEME', 'AQUI VA LA DESCRIPCION DEL MEME')

root.mainloop()
