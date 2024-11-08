@echo off


:start
cls



call config.bat
ngrok config add-authtoken %authtoken%

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install gitpython
pip install ngrok

python ./get_repo.py



pause
exit