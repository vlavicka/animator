if "%ENVDEFINED%" == "1" goto skip

set BOOST_ROOT=c:\develop\boost_1_49_0
set BOOST_LIBRARYDIR=%BOOST_ROOT%\stage\lib
set PATH=c:\MinGW\bin;c:\develop\CMake_2.8\bin;c:\develop\swigwin-2.0.4;c:\Python27;%BOOST_ROOT%;%BOOST_LIBRARYDIR%
set PYTHONPATH=%~d0%~p0\build\%1\swig

set ENVDEFINED=1
:skip
