import os
import sys
import subprocess
import venv
import platform
import notificaErrores
import pathlib

directorio_base = pathlib.Path(__file__).parent.parent
VENV_DIRECTORIO = ".fb_poster"

def crearAmbiente():
    venv.create(VENV_DIRECTORIO, with_pip=True)
    notificaErrores.notificaExito(titulo="Ambiente", mensaje="Ambiente virtual creado con exito")

def ejecutarAmbiente():
    if platform.system() == "Windows":
        python_bin = os.path.join(VENV_DIRECTORIO, "Scripts", "python.exe")
    else:
        python_bin = os.path.join(VENV_DIRECTORIO, "bin", "python")
    print(python_bin)
    if not os.path.exists(python_bin):
        notificaErrores.realizaNotificacion(mensaje="No se encontro el ejecutable del entorno virtual")
        sys.exit(1)

    reqDir = os.path.join(directorio_base,"requisitos.txt")
    if os.path.exists(reqDir):
        notificaErrores.notificaExito(titulo="Instalando",mensaje="Instalando dependencias desde archivo requisitos")
        subprocess.check_call([python_bin, "-m","pip","install","-r",reqDir])
    subprocess.check_call([python_bin, "interfaz.py"])

if __name__ == "__main__":
    if not os.path.exists(VENV_DIRECTORIO):
        crearAmbiente()
    ejecutarAmbiente()