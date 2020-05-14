import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from json import *


screenSize = {'width': 360, 'height': 800}


root = tk.Tk()
root.title('root')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)

seccion1 = tk.Frame(master=root, bg="green")
seccion1.place(relwidth=1.0, relheight=0.1, anchor=tk.NW)
seccion1.place_configure(relx=0, rely=0)

label1 = tk.Label(master=seccion1,
                  bg="green",
                  fg="white",
                  text="Lista de memes",
                  font=tkFont.Font(family='Roboto', size=20)
                  )
label1.place(anchor=tk.NW, relx=0.1, rely=0.2)

seccion2 = tk.Frame(master=root, bg="white")
seccion2.place(anchor=tk.NW, relwidth=1.0, relheight=0.9, relx=0, rely=0.1)

root.mainloop()