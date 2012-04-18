@echo off
setlocal

set PATH=c:\MinGW\bin;c:\develop\swigwin-2.0.4

swig -python -c++ test.i
mingw32-g++ -c test.cxx test_wrap.cxx -Ic:\Python27\include
mingw32-g++ -shared test.o test_wrap.o -o _test.pyd -L"c:\Python27\libs" -L"c:\MinGW\lib" -lpython27

:end
endlocal
@echo on
