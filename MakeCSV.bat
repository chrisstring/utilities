@echo off
cls
echo "This will EXCLUDE all files with a CSV file extension"
set /p filePath="Please PASTE the path to the folder that you want [shift] + [INS]:"
pushd %filePath%
dir /b | findstr /v /i "\.csv$" > filelist.csv
echo Operation successful, located at:%filePath%filelist.csv
