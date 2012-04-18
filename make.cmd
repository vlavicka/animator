@echo off
setlocal

set PATH=c:\MinGW\bin;c:\develop\CMake_2.8\bin;c:\develop\swigwin-2.0.4

rem swig -python test.i
cmake -G "MinGW Makefiles" --warn-uninitialized --warn-unused-vars -Wno-dev
mingw32-make 

test.exe

endlocal
@echo on
