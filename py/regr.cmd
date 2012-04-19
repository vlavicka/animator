@echo off
setlocal
call ..\env.cmd
c:\Python27\python.exe regr.py %*
endlocal
@echo on
