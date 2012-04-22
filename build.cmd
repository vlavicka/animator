@echo off
setlocal

call env.cmd
if not exist build mkdir build
pushd build
cmake -G "MinGW Makefiles" -D ANIMATOR_DEBUG:STRING=debug --warn-uninitialized --warn-unused-vars -Wno-dev ..
mingw32-make 
set BUILD_ERROR=%ERRORLEVEL%
popd

if %BUILD_ERROR% NEQ 0 goto error

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

goto end

:error
echo "Error while building!"

:end
endlocal
@echo on
