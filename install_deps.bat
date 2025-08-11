@echo off
REM Batch script to install Python (if needed) and required packages
echo ========================================
echo  SVG to Decal PDF - Dependency Installer
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python is already installed
    goto :install_packages
)

echo × Python not found. Installing Python automatically...
echo.

REM Create temp directory for download
if not exist "%TEMP%\svg-decal-installer" mkdir "%TEMP%\svg-decal-installer"
cd /d "%TEMP%\svg-decal-installer"

echo Downloading Python installer...
REM Download Python 3.11 (stable, widely compatible)
powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'python-installer.exe'}"

if not exist "python-installer.exe" (
    echo ✗ Failed to download Python installer
    echo Please manually install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Installing Python... (this may take a few minutes)
echo ⚠️  IMPORTANT: This will install Python with default settings and add it to PATH
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Clean up
del python-installer.exe
cd /d "%~dp0"

REM Refresh environment variables
call refreshenv >nul 2>&1 || (
    echo Please close and reopen this command prompt, then run this script again.
    pause
    exit /b 0
)

REM Check if Python installation succeeded
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ✗ Python installation may have failed
    echo Please manually install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python installed successfully!
echo.

:install_packages
echo Installing required Python packages...
python -m pip install --upgrade pip
python -m pip install reportlab svglib

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo  ✓ Installation Complete!
    echo ========================================
    echo You can now run the decal generator:
    echo   • Double-click: run_decal_generator.bat
    echo   • Command line: python make_decals_sheet.py your_file.svg
    echo.
) else (
    echo.
    echo ✗ Package installation failed
    echo Please try running: python -m pip install reportlab svglib
    echo.
)

pause