@echo off

set OLDDIR=%CD%

:start
cls

call config.bat


echo Getting new files (takes a long time for the first time):
echo Getting files for world: %currrent_world%

cd ..

git fetch origin %currrent_world%
git reset --hard origin/%currrent_world%

echo Type 'stop' into this terminal when you want to end the server!

chdir /d %OLDDIR% &rem restore current directory
@REM python ./update_pull.py

start "" ngrok tcp --region=au --remote-addr=1.tcp.au.ngrok.io:20478 25565

call run.bat

:exit

taskkill.exe /IM ngrok.exe /F 

echo Upping files:

set /p upload_name=Enter name to use for upload:  

echo Setting everything up... The first time could take a while

cd ..

git status
git add .
git commit . -m "Update from %upload_name%"



echo Wait until this terminal says 'complete'

git push -u origin HEAD:%currrent_world%

echo Complete

echo                    YAao,
echo                     Y8888b,
echo                   ,oA8888888b,
echo             ,aaad8888888888888888bo,
echo          ,d888888888888888888888888888b,
echo        ,888888888888888888888888888888888b,
echo       d8888888888888888888888888888888888888,
echo      d888888888888888888888888888888888888888b
echo     d888888P'                    `Y888888888888,
echo     88888P'                    Ybaaaa8888888888l
echo    a8888'                      `Y8888P' `V888888
echo  d8888888a                                `Y8888
echo AY/'' `\Y8b                                 ``Y8b
echo Y'      `YP                                    ~~
echo          `'


@REM python ./update_push.py



PAUSE