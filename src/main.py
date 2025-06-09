import os
import sys
import subprocess
import venv
import platform
import notificaErrores
import pathlib
import argparse

directorio_base = pathlib.Path(__file__).parent.parent
VENV_DIRECTORIO = ".fb_poster"

def crearAmbiente():
    venv.create(VENV_DIRECTORIO, with_pip=True)
    notificaErrores.notificaExito(titulo="Ambiente", mensaje="Ambiente virtual creado con exito")

def ejecutarAmbiente(modoEjecucion):
    if platform.system() == "Windows":
        if modoEjecucion:
            python_bin = os.path.join(VENV_DIRECTORIO, "Scripts", "pythonw.exe")
        else:
            python_bin = os.path.join(VENV_DIRECTORIO, "Scripts", "python.exe")
    else:
        python_bin = os.path.join(VENV_DIRECTORIO, "bin", "python")
    print(python_bin)
    if not os.path.exists(python_bin):
        notificaErrores.notificaError(mensaje="No se encontro el ejecutable del entorno virtual")
        sys.exit(1)

    reqDir = os.path.join(directorio_base,"requisitos.txt")
    if os.path.exists(reqDir):
        notificaErrores.notificaExito(titulo="Instalando",mensaje="Instalando dependencias desde archivo requisitos")
        subprocess.check_call([python_bin, "-m","pip","install","-r",reqDir])
    subprocess.check_call([python_bin, "interfaz.py"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sinconsola", action="store_true", help="Ejecuta la app en segundo plano sin print a consola")
    args = parser.parse_args()
    if not os.path.exists(VENV_DIRECTORIO):
        crearAmbiente()
    if args.sinconsola:
        ejecutarAmbiente(True)
    else:
        ejecutarAmbiente(False)