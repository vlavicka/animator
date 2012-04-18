@echo off
setlocal
call env.cmd

g++ -o test.exe test.cpp src\model\layer.cpp

test.exe

:end
endlocal
@echo on
