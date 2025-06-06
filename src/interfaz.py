from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import posteo
import notificaErrores

def creaIcono():
    imagen = Image.new("RGB", (64,64), color=(255,255,255))
    d = ImageDraw.Draw(imagen)
    d.rectangle((16,16,48,48), fill=(0,0,0))
    return imagen

def publicaImagenes():
    posteo.realizaPosteoImagen()

def salir(icon):
    icon.stop()

icon = Icon(
    "publicaFB",
    icon = creaIcono(),
    title = "Autom FB",
    menu = Menu(
        MenuItem("Postea en FB", publicaImagenes),
        MenuItem("Salir", salir)
    )
)

notificaErrores.notificaExito(titulo="Exito",mensaje="Aplicación corriendo en segundo plano")
icon.run()

