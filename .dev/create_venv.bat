cd ..

REM ########################
REM # Install Virtual Env  #
REM ########################
C:\Python312_64\python.exe -m venv .venv

REM ########################
REM # Active Virtual Env   #
REM ########################
call .venv\scripts\activate.bat

REM ########################
REM # Updrade Setuptools   #
REM ########################
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip

REM ########################
REM # INSTALL OTHER PACKAGES#
REM ########################
pip install -r src\requirements.txt
pip install -r src\requirements_dev.txt
pause