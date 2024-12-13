@echo off
setlocal enabledelayedexpansion

REM Obtém o caminho da pasta onde o arquivo BAT está localizado
set "basepath=%~dp0"

REM Renomeia todas as pastas e subpastas primeiro
for /f "delims=" %%D in ('dir /ad /b /s "%basepath%"') do (
    set "folder=%%~nxD"
    set "path=%%~dpD"
    set "newfolder=!folder:-=_!"
    if not "!folder!"=="!newfolder!" (
        ren "%%D" "!newfolder!"
    )
)

REM Renomeia todos os arquivos dentro das pastas e subpastas
for /f "delims=" %%F in ('dir /a-d /b /s "%basepath%"') do (
    set "file=%%~nxF"
    set "path=%%~dpF"
    set "newfile=!file:-=_!"
    if not "!file!"=="!newfile!" (
        ren "%%F" "!newfile!"
    )
)

echo Renomeação concluída para pastas, subpastas e arquivos.
pause
