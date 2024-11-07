@echo off

python ./update_pull.py


java -Xmx3072M -Xms3072M -jar server.jar nogui



PAUSE

python ./update_push.py

PAUSE
