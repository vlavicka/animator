@echo off
setlocal

call env.cmd
if not exist build mkdir build
pushd build
cmake -G "MinGW Makefiles" --warn-uninitialized --warn-unused-vars -Wno-dev ..
mingw32-make 
rem mingw32-make test
popd

if not "%1" == "notest" (
    echo.
    echo -----------------------------------------------------------------------
    echo R u n n i n g   P Y T H O N   r e g r e s s i o n   t e s t s
    echo -----------------------------------------------------------------------
    echo.
    pushd py
    call regr.cmd
    @echo off
    popd
)

endlocal
@echo on
