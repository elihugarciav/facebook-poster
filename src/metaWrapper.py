import requests
from dotenv import load_dotenv
import os

load_dotenv()

id_pagina = os.getenv("meta_id_pagina")
token = os.getenv("meta_token_acceso")
url = f"https://graph.facebook.com/{id_pagina}/photos"

def realizaPosteo(dirImagen, descripcion):
    parametros = {
        "access_token": token,
        "caption": descripcion
    }
    try:

        with open(dirImagen, "rb") as img:
            files ={"source": img}
            response = requests.post(url, params=parametros,files=files)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'id' in data:
                id_post = data["id"]
                
                return{
                    "exito_post": True,
                    "mensaje_estado": f"Publicacion exitosa id: {id_post}\n Imagen: {dirImagen}"
                }
            else:
                 return{
                    "exito_post": False,
                    "mensaje_estado": "No se recibio id de publicacion, aunque el consumo de la api de meta fue exitosa"
                }
        else:
            data_err = response.json()
            return {
                "exito_post": False,
                "mensaje_estado": f'Comunicacion no exitosa:\n {data_err["error"]["message"]}'
            }
    
    except FileNotFoundError as fne:
        print(fne)
        return{
            "exito_post": False,
            "mensaje_estado": f"Imagen no encontrada: {dirImagen}"
        }
    except Exception as e:
        print(e)
        return{
            "exito_post": False,
            "mensaje_estado": f"Error inesperado: {e}"
        }
    