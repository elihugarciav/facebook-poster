import os
import shutil

def buscaImagenes(directorio):
    extensiones = {".jpg",".jpeg",".png",".gif",".webp",".bmp"}
    
    lista_imagenes = []

    for nombre in os.listdir(directorio):
        _, exten  = os.path.splitext(nombre)
        if exten.lower() in extensiones:
            lista_imagenes.append(nombre)

    return lista_imagenes

def mueveImagen(origen, destino):
    try:
        shutil.move(origen,destino)
        return {
            "movida": True,
            "mensaje": "Imagen procesada y movida a carpeta procesadas"
        }
    except FileNotFoundError as fne:
        print(fne)
        return{
            "movida": False,
            "mensaje": "imagen procesada no encontrada"
        }
    except Exception as e:
        print(e)
        return{
            "movida": False,
            "mensaje": "error al mover imagen procesada "
        }
