import requests
import urllib


def download_image(name, link):
    opener = urllib.request.URLopener()
    # engañar a imgflip para que crea que es un usaurio real
    opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72')
    # es más fácil descargar cosas con urllib
    extension = link.split(".")[-1]
    opener.retrieve(link, name+"."+extension)# se me olvidó cambiar aqui el nombre de la variable
    return name+"."+extension


if __name__ == "__main__":
    download_image("meme", "https://i.imgflip.com/1ur9b0.jpg")
    print("descargado")