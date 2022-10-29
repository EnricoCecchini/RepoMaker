@echo off
pushd %~dp0
: Check python install
: Create Venv
: Activate Venv
: pip install selenium
: pip install webdriver-manager
: Run python script

set script=%cd%\main.py
set scriptPath=%cd%
set "virtual_env=env"
set project_title = %~1

echo %script%
echo %project_title%

if not exist %virtual_env% (
    echo Creating virtual environment...
    python -m venv %virtual_env% 
    CALL %virtual_env%\Scripts\activate.bat & pip install -r requirements.txt
)

CALL %virtual_env%\Scripts\activate.bat

:activate_venv
set PYTHON = %virtual_env%\Scripts\Python.exe
: env\Scripts\activate
: pip install selenium
: pip install webdriver_manager

popd
set project_path=%cd%
echo project_path

:run
%virtual_env%\Scripts\Python.exe %script% %~1 %project_title% "%scriptPath%" "%project_path%"
code .
pause
