if "%ENVDEFINED%" == "1" goto skip

set OPENDEVDIR=c:\opendev
set BOOST_ROOT=%OPENDEVDIR%\boost_1_49_0
set BOOST_LIBRARYDIR=%BOOST_ROOT%\stage\lib
set PATH=%OPENDEVDIR%\MinGW\bin;%OPENDEVDIR%\CMake_2.8\bin;%OPENDEVDIR%\swigwin-2.0.6;c:\Python27;%BOOST_ROOT%;%BOOST_LIBRARYDIR%
set PYTHONPATH=%~d0%~p0\build\%1\swig

set ENVDEFINED=1
:skip
