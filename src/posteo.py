import procesaimagen
import pathlib
import geminiWrapper as gemini
import metaWrapper as meta
import archivosManejador as archman
import notificaErrores

base = pathlib.Path(__file__).parent

def realizaPosteoImagen():
    prompt = archman.leerArchivoPrompt("prompt.txt")
    if not prompt["existe"]:
        notificaErrores.notificaError(prompt["contenido"])
        return
        
    lista = procesaimagen.buscaImagenes(base.parent/"imagenes")
    if lista:
        print("Imagenes encontradas: ",lista)
        dirImagen = base.parent/"imagenes"/lista[0]
        print("Imagen a ser procesada: ", dirImagen)
        respuestaGemini = gemini.generaDescIma(nombre_imagen=dirImagen, prompt=prompt["contenido"])
        if respuestaGemini["exito"]:
            print("Respuesta gemini:\n",respuestaGemini["texto"])
            respuestaMeta = meta.realizaPosteo(dirImagen=dirImagen, descripcion=respuestaGemini["texto"])
            print("Respuesta Meta:\n",respuestaMeta)
            if respuestaMeta["exito_post"]:
                notificaErrores.notificaExito("Publicacicón en Facebook exitosa!",respuestaMeta["mensaje_estado"])
                respuestaImagen =  procesaimagen.mueveImagen(dirImagen,base.parent/"procesadas")
                if respuestaImagen["movida"]:
                    notificaErrores.notificaExito(titulo="Imagen procesada!",mensaje=respuestaImagen["mensaje"])
                else:
                    notificaErrores.notificaError(respuestaImagen["mensaje"])
            else:
                notificaErrores.notificaError(respuestaMeta["mensaje_estado"])
        else:
            notificaErrores.notificaError(respuestaGemini["texto"])
    else:
        notificaErrores.notificaError("No se encontro ninguna imagen")
        

