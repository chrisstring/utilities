@echo off
cls
echo "This will EXCLUDE all files with a CSV file extension"
set /p filePath="Please PASTE the path to the folder that you want using [shift] + [INS]:"
pushd %filePath%
for /r %%i in (*) do @echo %%~nxi >> filelist.csv
echo Operation successful, located at:%filePath%filelist.csv
pause
