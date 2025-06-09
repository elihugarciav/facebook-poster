@echo off


wmic process where "name='pythonw.exe'" get CommandLine 2>nul | find /i "main.py" >nul
if %errorlevel%==0 (
    echo La aplicacion ya esta corriendo.
    pause
    exit /b
)
set AMBIENTE=.fb_poster
set "RUTA_BASE=%~dp0"
set "REQUI=%RUTA_BASE%requisitos.txt"
cd src
python -m venv %AMBIENTE%
call %AMBIENTE%\Scripts\activate.bat
pip install -r %REQUI%
start "" .fb_poster\Scripts\pythonw.exe main.py --sinconsola