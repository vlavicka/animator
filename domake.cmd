@echo off
setlocal

set PATH=c:\MinGW\bin;c:\develop\CMake_2.8\bin;c:\develop\swigwin-2.0.4;%PATH%

cmake -G "MinGW Makefiles" --warn-uninitialized --warn-unused-vars -Wno-dev
mingw32-make 

python -c "import animator; print animator.myvalue()"

mainapp.exe

endlocal
@echo on
