import procesaimagen
import pathlib
import geminiWrapper as gemini
import metaWrapper as meta
import notificaErrores

base = pathlib.Path(__file__).parent

def realizaPosteoImagen():
    lista = procesaimagen.buscaImagenes(base.parent/"imagenes")
    if lista:
        print(lista)
        dirImagen = base.parent/"imagenes"/lista[0]
        respuestaGemini = gemini.generaDescIma(dirImagen)
        if respuestaGemini["exito"]:
            print(respuestaGemini["texto"])
            respuestaMeta = meta.realizaPosteo(dirImagen=dirImagen, descripcion=respuestaGemini["texto"])
            print(respuestaMeta)
            if respuestaMeta["exito_post"]:
                notificaErrores.notificaExito("Publicacicón en Facebook exitosa!",respuestaMeta["mensaje_estado"])
                respuestaImagen =  procesaimagen.mueveImagen(dirImagen,base.parent/"procesadas")
                if respuestaImagen["movida"]:
                    notificaErrores.notificaExito(titulo="Imagen procesada!",mensaje=respuestaImagen["mensaje"])
                else:
                    notificaErrores.realizaNotificacion(respuestaImagen["mensaje"])
            else:
                notificaErrores.realizaNotificacion(respuestaMeta["mensaje_estado"])
        else:
            notificaErrores.realizaNotificacion(respuestaGemini["texto"])
    else:
        notificaErrores.realizaNotificacion("No se encontro ninguna imagen")
        

