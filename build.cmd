@echo off
setlocal enabledelayedexpansion

if not exist build mkdir build
set CMAKE_DEBUG=1

if "%1" == "" (set BUILD_MODE=Release) else (set BUILD_MODE=%1)
set BUILD_DIR=build\!BUILD_MODE!
if not exist !BUILD_DIR! mkdir !BUILD_DIR!

call env.cmd !BUILD_MODE!

call :caption "P r o c e s s i n g   C M A K E   f i l e"
call :execute cmake -G "MinGW Makefiles" -D ANIMATOR_DEBUG:STRING=debug --warn-uninitialized --warn-unused-vars -Wno-dev ..\..

call :caption "B u i l d i n g   p r o j e c t"
call :execute mingw32-make
if "%ERRORLEVEL%" == "1" goto error

call :caption "R U N N I N G   U N I T   T E S T S"
call :execute tests\layer_test 

if not "%1" == "notest" (
    call :caption "R u n n i n g   P Y T H O N   r e g r e s s i o n   t e s t s"
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
exit /b

:execute 
pushd !BUILD_DIR!
call %*
if "%ERRORLEVEL%" == "1" (set RETVAL=1) else (set RETVAL=0)
popd
exit /b !RETVAL!


:caption 
echo.
echo -----------------------------------------------------------------------
echo %~1
echo -----------------------------------------------------------------------
echo.
exit /b

