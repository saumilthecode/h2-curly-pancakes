"%~dp0lib\python-3.13.7-amd64.exe" /quiet /uninstall
if exist "%ProgramFiles%\Python313\" rd /s /q "%ProgramFiles%\Python313\"
if exist "%ProgramFiles%\DB Browser for SQLite\Uninstall.exe" (
    "%ProgramFiles%\DB Browser for SQLite\Uninstall.exe" /S
) 
if exist "%ProgramFiles%\Notepad++\uninstall.exe" (
    "%ProgramFiles%\Notepad++\uninstall.exe" /S
) 