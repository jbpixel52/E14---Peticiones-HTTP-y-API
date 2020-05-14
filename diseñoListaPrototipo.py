import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from json import *


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
    


class meme(app):
    def __init__(self, master, titulo):
        super().__init__(master, titulo)

class lista(app):
    def __init__(self, master, titulo):
        super().__init__(master, titulo)


lista_memes = lista(root, 'LISTA DE MEMES')

root.mainloop()
