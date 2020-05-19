import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from json import *
from io import BytesIO
import requests  # Importando requests

from ImageDownloader import download_image

leer_json = open('NombreDelJsons.json', 'r')  # Funcion para leer json
URL = 'https://api.imgflip.com/get_memes'
r = requests.get(URL)
top_15 = []
index_of_clicked = 0

link_imagenes = {
    "Distracted Boyfriend": "https://i.imgflip.com/1ur9b0.jpg",
    "Drake Hotline Bling": "https://i.imgflip.com/30b1gx.jpg",
    "Two Buttons": "https://i.imgflip.com/1g8my4.jpg",
    "Batman Slapping Robin": "https://i.imgflip.com/9ehk.jpg",
    "Expanding Brain": "https://i.imgflip.com/1jwhww.jpg",
    "Uno Draw 25 Cards": "https://i.imgflip.com/3lmzyx.jpg",
    "Running Away Balloon": "https://i.imgflip.com/261o3j.jpg",
    "Change My Mind": "https://i.imgflip.com/24y43o.jpg",
    "Mocking Spongebob": "https://i.imgflip.com/1otk96.jpg",
    "Is This A Pigeon": "https://i.imgflip.com/1o00in.jpg",
    "Inhaling Seagull": "https://i.imgflip.com/1w7ygt.jpg",
    "Left Exit 12 Off Tamp": "https://i.imgflip.com/22bdq6.jpg",
    "Woman Yelling At Cat": "https://i.imgflip.com/345v97.jpg",
    "American Chopper Argument": "https://i.imgflip.com/2896ro.jpg",
    "Epic Handshake": "https://i.imgflip.com/28j0te.jpg"
}

descripciones_memes = {
    "Distracted Boyfriend": "Boyfriend distracted by another girl",
    "Drake Hotline Bling": "Drake reacting negatively to one thing and positively to another",
    "Two Buttons": "Someone having a hard time deciding between two buttons",
    "Batman Slapping Robin": "Batman slaps Robin",
    "Expanding Brain": "An expanding brain according to different decisions",
    "Uno Draw 25 Cards": "Someone drawing 25 UNO to avoid doing something",
    "Running Away Balloon": "Trying to grab a balloon, but being stopped",
    "Change My Mind": "Someone challenges you to change his mind about something",
    "Mocking Spongebob": "Spongebob mocking something",
    "Is This A Pigeon": "Someone thinking a butterfly is a pigeon",
    "Inhaling Seagull": "Seagull inhaling to scream",
    "Left Exit 12 Off Tamp": "Someone taking the exit 12",
    "Woman Yelling At Cat": "Woman yelling at cat",
    "American Chopper Argument": "Argument between two guys",
    "Epic Handshake": "Epic Handshake from Predator"
}


name_of_meme = ''
datos_json = loads(r.text)


# print(datos_json)
count = 0
for i in datos_json['data']['memes']:
    print(i['name'])

    if count < 15:
        top_15.append(i)

    elif count > 15:
        break
    count += 1

'''RECUERDEN COMENTAR SUS CAMBIOS'''

screenSize = {'width': 360, 'height': 800}
root = tk.Tk()
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)
pepe = ImageTk.PhotoImage(Image.open('Pepe.png').resize((65, 65)))


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


img_meme = None # evitar que el recolector de basura borre la imagen


class meme(app):  # AGREGUE EL FORMATO PARA LA VENTANA DONDE MUESTRA EL MEME
    def __init__(self, master, titulo,url_imagen, descripcion_del_meme):
        super().__init__(master, titulo)
        

        """
        respuesta = requests.get(url_imagen, stream = True)
        
        
        with open('meme.png','wb') as file: #hacer que descargue la imagen del meme
            for chunk in respuesta.iter_content():
                file.write(chunk)
        """ ## En lugar de usar esto usamos el download_image
        filename = download_image('meme', url_imagen) # en teoría debería de funcoinar

        global img_meme
        img_meme = ImageTk.PhotoImage(Image.open(filename).resize((300, 360)))
        self.canvas = tk.Canvas(self.cuerpo, bg="black", width=300, height=360)
        self.canvas.place(anchor=tk.NW, relx=0.075, rely=0.1)
        # self.canvas.create_image(0,0,image=imagen)
        self.canvas.create_image(0, 0, image=img_meme, anchor=tk.NW)

        root.update_idletasks()

        self.Descripcion = tk.Message(self.cuerpo,
                                      bg='white',
                                      fg = 'black',
                                      text= descripcion_del_meme,
                                      font=tkFont.Font(
                                          family='Roboto', size=15)
                                      )
        self.Descripcion.place(anchor=tk.NW, relx=0.1, rely=0.65)
        self.Regresar = tk.Button(self.cuerpo,
                                  bg='white',
                                  text='Regresar',
                                  font=tkFont.Font(family='Roboto', size=15),
                                  command=lista_memes.screen.tkraise  # Comando al boton
                                  )
        self.Regresar.place(anchor=tk.NW, relx=0.4, rely=0.9)


class lista(app):
    def __init__(self, master, titulo):
        super().__init__(master, titulo)

        self.canvas = tk.Canvas(
            self.encabezado, bg="black", width=75, height=75)
        self.canvas.place(anchor=tk.NW, relx=0.75, rely=0.02)
        self.canvas.create_image(0, 0, image=pepe, anchor=tk.NW)
        # creates list to replace your actual inputs for troubleshooting purposes
        self.meme_list = []
        self.btn_list = []  # creates list to store the buttons ins

    def buttons(self):
        # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
        for item in range(15):
            # aqui en vez de i, meteriamos el nombre del meme
            self.meme_list.append((top_15[item]['name']))

        # this says for *counter* in *however many elements there are in the list files*
        for i in range(len(self.meme_list)):
            # the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
            self.btn_list.append(tk.Button(
                self.cuerpo, bg='white',
                font=tkFont.Font(family='Roboto', size=15), text=self.meme_list[i], command=lambda c=i: self.click(c)))
            self.btn_list[i].pack()  # this packs the buttons

    def click(self, c):
        name_of_meme = self.btn_list[c].cget('text')
        index_of_clicked = c
        url_imagen = link_imagenes[name_of_meme]
        descripcion_del_meme = descripciones_memes[name_of_meme]

        print(url_imagen)

        vista_memes = meme(root, name_of_meme, url_imagen, descripcion_del_meme)
        root.update_idletasks()
        vista_memes.screen.tkraise()
        root.update_idletasks()


lista_memes = lista(root, 'TOP 15 MEMES')
# Aqui forma la ventana del meme
lista_memes.buttons()
lista_memes.screen.tkraise()

root.mainloop()
