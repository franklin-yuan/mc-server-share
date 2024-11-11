@echo off

set OLDDIR=%CD%

:start
cls


@REM python ./get-pip.py

@REM cd \
@REM cd \python%python_ver%\Scripts\
@REM pip install gitpython
@REM pip install ngrok

cd .. 
git init
git remote add origin https://github.com/franklin-yuan/mc-server-share.git
git status
git fetch --all
git reset --hard origin/main

echo:
echo:

echo Please select which world you would like to host. The current worlds include:
echo Current worlds include:

git branch -r
echo Entering one that is not in the list will create a new world of that name.
set /p world=Enter world (without the 'origin/', etc main): 



git branch -M %world%

git checkout -f %world%

echo Currently on:

git branch

chdir /d %OLDDIR% &rem restore current directory

@REM python ./get_repo.py

echo set currrent_world=%world%> config.bat

echo We need your ngrok authentication token (authtoken) now. Please make sure you have signed up and have your authtoken ready.
set /p authtoken=Authtoken: 
echo We need an email for git to use. Please enter your email: 
set /p user_email=Email: 
set user_email=%user_email: =%
echo We need a username for git to use. Please enter a username: 
set /p user_name=Username:  

ngrok config add-authtoken %authtoken%
git config --global user.email %user_email%
git config --global user.name %user_name%



pause
exit