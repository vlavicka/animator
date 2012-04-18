setlocal
set PATH=c:\develop\swigwin-2.0.4;c:\MinGW\bin;%PATH%

set INCLUDE_PYTHON=c:\Python27\include
set LIB_PYTHON=c:\Python27\libs

swig -c++ -python animator.i
g++ -c animator.cxx testcxx_wrap.cxx -I%INCLUDE_PYTHON%
g++ -shared animator.o testcxx_wrap.o -o _testcxx.pyd -L%LIB_PYTHON% -lpython27
python -c "import animator; print 'TEST animator.x() -> ' + str(animator.myvalue())"

endlocal
