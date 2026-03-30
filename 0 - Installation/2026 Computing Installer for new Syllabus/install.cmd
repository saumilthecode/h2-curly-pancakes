@echo off

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrator rights.
    echo Please right-click and "Run as administrator".
    pause
    exit /b 1
)

setlocal

echo [7mSTEP 0 of 5: Uninstall existing applications[0m
echo - Running uninstall.cmd ...
call "%~dp0uninstall.cmd"
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mSTEP 1 of 5: Install Python[0m
echo - Installing Python 3.13.7 ...
"%~dp0lib\python-3.13.7-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 DefaultAllUsersTargetDir="%ProgramFiles%\Python313"
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mSTEP 2 of 5: Install Python modules[0m
set "PIP=%ProgramFiles%\Python313\Scripts\pip.exe"
echo - Removing preinstalled packages ...
"%PIP%" uninstall -y flask jupyterlab scikit-learn matplotlib pandas
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])
echo - Installing from local modules ...
"%PIP%" install -q --no-index --no-warn-script-location -f "%~dp0modules" flask jupyterlab scikit-learn matplotlib pandas
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mSTEP 3 of 5: Add JupyterLab shortcut[0m
echo - Creating shortcut ...
cscript //nologo "%~dp0lib\install-jupyterlab-shortcut.vbs"
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mSTEP 4 of 5: Install DB Browser for SQLite[0m
echo - Installing DB Browser for SQLite ...
"%~dp0lib\DB.Browser.for.SQLite-3.10.1-win64.exe" /S
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mSTEP 5 of 5: Install Notepad++[0m
echo - Installing Notepad++ ...
"%~dp0lib\npp.8.9.1.Installer.x64.exe" /S
if errorlevel 1 (echo   [[91mERROR[0m]) else (echo   [[92mOK[0m])

echo [7mINSTALLATION COMPLETE[0m
timeout /t 5 >nul

endlocal