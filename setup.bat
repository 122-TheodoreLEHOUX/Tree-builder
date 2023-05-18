@echo off

REM setup virtual environmnent. Note: set python version X.X on initial setup
py -3.10 -m venv venv

REM activate virtual environment
call venv\Scripts\activate.bat

REM install dependencies into virtual environment
pip install -r requirements.txt