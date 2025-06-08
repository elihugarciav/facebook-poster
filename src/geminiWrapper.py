import google.generativeai as gemini
from google.api_core.exceptions import GoogleAPICallError, PermissionDenied, InvalidArgument
import pathlib
import PIL.Image
import os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("google_api_key")
modelo_empleado = os.getenv("modelo_gemini")

def generaDescIma(nombre_imagen, prompt):
    gemini.configure(api_key=key)
    model = gemini.GenerativeModel(modelo_empleado)

    imagen = PIL.Image.open(pathlib.Path(nombre_imagen))
    
    try:
        response = model.generate_content([prompt, imagen])
        if response.text:
            return {
                "exito": True,
                "texto": response.text
            }
        else:
            return {
                "exito": False,
                "texto": "No se recibio respuesta de Gemini"
            }
    except InvalidArgument as inva:
        print(inva)
        return {
                "exito": False,
                "texto": "Error en prompt argumento invalido"
        }
        
    except PermissionDenied as pd:
        print(pd)
        return {
                "exito": False,
                "texto": "Accesso denegado por Gemini revisa tu clave API"
        }
        
    except GoogleAPICallError as ge:
        print(ge)
        return {
                "exito": False,
                "texto": "Error al llamar la API de Gemini intenta más tarde"
        }
    except Exception as e:
        print(e)
        return {
                "exito": False,
                "texto": "Error inesperado al emplear API de Gemini"
        }
    
