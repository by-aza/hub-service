@echo off
echo ================================
echo Pornesc serverul local pentru HUB
echo ================================
echo.

REM NOTE: setează folderul în care se află consumabile.html
cd /d "D:\_GitHub\hub-service-dev\modules\stocuri"

REM NOTE: încearcă să pornească serverul cu python
python -m http.server 8000

REM Dacă python nu merge, încearcă py
if %errorlevel% neq 0 (
    py -m http.server 8000
)

pause