@echo off
: Check python install
: Create Venv
: Activate Venv
: pip install selenium
: pip install webdriver-manager
: Run python script

set script=%cd%\main.py
echo %script%

set "virtual_env=env"

if not exist %virtual_env% (
    echo Creating virtual environment...
    python -m venv %virtual_env%
)

CALL %virtual_env%\Scripts\activate.bat

pip install virtualenv
virtualenv env
env\Scripts\activate
pip install selenium
pip install webdriver_manager
"C:\Users\Enric\AppData\Local\Programs\Python\Python310\python.exe" %script%
pause