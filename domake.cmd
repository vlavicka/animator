@echo off
setlocal

call env.cmd

cmake -G "MinGW Makefiles" --warn-uninitialized --warn-unused-vars -Wno-dev
mingw32-make 
rem mingw32-make test

echo.
echo -----------------------------------------------------------------------
echo R U N N I N G   p y t h o n   r e g r e s s i o n   t e s t s
echo -----------------------------------------------------------------------
echo.
pushd py
call regr.cmd
@echo off
popd

endlocal
@echo on
