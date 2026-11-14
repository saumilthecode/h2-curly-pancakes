' Adapted from https://gist.github.com/rcmdnk/7631748

' Set basic objects
Set wssh = WScript.CreateObject("WScript.Shell")
Set fs = WScript.CreateObject("Scripting.FileSystemObject")

' Basic Values
progFiles = "%ProgramFiles%\Python313\Scripts"
startMenu = wssh.SpecialFolders("AllUsersPrograms")
pExe = "jupyter-lab.exe"

' Make start menu shortcut
Set oMyShortCut = wssh.CreateShortcut(startMenu & "\JupyterLab.lnk")
oMyShortCut.TargetPath = progFiles & "\" & pExe
oMyShortCut.Arguments = "--notebook-dir=""%USERPROFILE%\Desktop"""
oMyShortCut.Save
