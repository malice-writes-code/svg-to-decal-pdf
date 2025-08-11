@echo off
REM Batch script to run the decal generator

REM Prompt for SVG filename
set /p SVGFILE=Enter the name of your SVG file (e.g. your_decal.svg): 

REM Prompt for output PDF filename
set /p PDFFILE=Enter the desired output PDF filename (or leave blank for default): 

REM Run the Python script
if "%PDFFILE%"=="" (
    python make_decals_sheet.py "%SVGFILE%"
) else (
    python make_decals_sheet.py "%SVGFILE%" --output "%PDFFILE%"
)

pause
