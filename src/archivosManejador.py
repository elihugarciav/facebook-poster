def leerArchivoPrompt(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            if not contenido.strip():
                return {
                    "existe": False,
                    "contenido": f"Prompt vacio: {ruta}"
                }
            return {
                "existe": True,
                "contenido": contenido
            }
    except FileNotFoundError as fne:
        print(fne)
        return {
                    "existe": False,
                    "contenido": "Archivo para prompt no encontrado"
                }
    except PermissionError as pe:
        print(pe)
        return {
                    "existe": False,
                    "contenido": f"No tienes permisos para visualizar este archivo: {ruta}"
                }
    except UnicodeDecodeError as ue:
        print(ue)
        return {
                    "existe": False,
                    "contenido": "Archivo no codificado en UTF-8"
                }
    except Exception as e:
        print(e)
        return {
                    "existe": False,
                    "contenido": f"Error inesparado al leer el archivo {ruta}"
                }