if "%ENVDEFINED%" == "1" goto skip

set PATH=c:\MinGW\bin;c:\develop\CMake_2.8\bin;c:\develop\swigwin-2.0.4;%PATH%
set PYTHONPATH=%~d0%~p0\build

set ENVDEFINED=1
:skip
