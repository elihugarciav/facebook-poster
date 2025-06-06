from plyer import notification

def realizaNotificacion(mensaje):
    notification.notify(
            title="Error",
            message=mensaje,
            timeout=3
        )
    
def notificaExito(titulo, mensaje):
    notification.notify(
        title=titulo,
        message=mensaje,
        timeout = 4
    )