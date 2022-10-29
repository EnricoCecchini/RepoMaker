@echo off
pushd %~dp0
: Check python install
: Create Venv
: Activate Venv
: pip install selenium
: pip install webdriver-manager
: Run python script

: Save path to script and bat file
set script=%cd%\main.py
set scriptPath=%cd%
: set venv path
set "virtual_env=env"
: Get project title from user
set project_title = %1

: Create venv if it doesn't exist and isntall dependencies
if not exist %virtual_env% (
    echo Creating virtual environment...
    python -m venv %virtual_env% 
    : Activate venv and install packages
    CALL %virtual_env%\Scripts\activate.bat & pip install -r requirements.txt
)

: Activate venv
CALL %virtual_env%\Scripts\activate.bat

: Set Python path
set PYTHON = %virtual_env%\Scripts\Python.exe

: Get path where prject will be clones
popd
set project_path=%cd%
echo %project_path%\%project_title%
: echo project_path

: Run python script
%virtual_env%\Scripts\Python.exe %script% %~1 %project_title% "%scriptPath%" "%project_path%"

: Open VS Code
cd "%project_path%"\%~1
code .
pause
