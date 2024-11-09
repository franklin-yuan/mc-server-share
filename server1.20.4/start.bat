@echo off

python ./update_pull.py

start "" ngrok tcp 25565 --region au

java -Xmx3072M -Xms3072M -jar server.jar nogui

taskkill.exe /IM ngrok.exe /F 

python ./update_push.py



PAUSE
