@echo off
setlocal enabledelayedexpansion

REM Set the fixed location
set "folder_location=D:\Desktop_files\Hobby_Coding\DataStructures\Problems"

REM Prompt for folder name
set /p folder_name=Enter folder name:

:: Initialize a variable to store the first word (problem number)
set problem_num=
set problem_name=
set "string_length=0"

:: Use a for loop to split the input sentence
for %%A in (!folder_name!) do (
    if not defined problem_num (
        set "problem_num=%%A"
    ) else (
        set "problem_name=!problem_name! %%A"
        set /a "string_length+=1"
    )
)

set "problem_name=!problem_name:~1!"

REM Create the folder at the fixed location
mkdir "!folder_location!\!problem_name!"

REM Create two sample files inside the folder
echo. > "!folder_location!\!problem_name!\README.md"
echo # !problem_num! !problem_name! > "!folder_location!\!problem_name!\README.md"
echo. > "!folder_location!\!problem_name!\solution.py"
:: echo Sample content for file 2 > "!folder_location!\!folder_name!\solution.py"
type "!folder_location!\sample.py" > "!folder_location!\!problem_name!\solution.py"

echo Folder "!problem_name!" created at "!folder_location!" with two sample files.
pause
