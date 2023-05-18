@echo off

rmdir /s /q dist

REM Build executable
pyinstaller project.spec

REM copy the config folder to the build output
mkdir dist\config
Xcopy config dist\config /E

