from plyer import notification

def validaLongMensaje(mensaje):
    if len(mensaje) > 255:
        print("texto supera caracteres permitidos:\n",mensaje)
        mensaje = mensaje[:256]
    return mensaje

def notificaError(mensaje):
    mensaje = validaLongMensaje(mensaje=mensaje)
    notification.notify(
            title="Error",
            message=mensaje,
            timeout=3
        )
    
def notificaExito(titulo, mensaje):
    mensaje = validaLongMensaje(mensaje=mensaje)
    notification.notify(
        title=titulo,
        message=mensaje,
        timeout = 4
    )