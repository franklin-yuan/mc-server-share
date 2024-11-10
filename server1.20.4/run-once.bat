@echo off

set OLDDIR=%CD%

:start
cls


python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install gitpython
pip install ngrok

chdir /d %OLDDIR% &rem restore current directory

python ./get_repo.py

call config.bat
ngrok config add-authtoken %authtoken%
git config --global user.email %user_email%
git config user.email %user_name%





pause
exit