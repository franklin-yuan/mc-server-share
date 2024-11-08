@echo off


:start
cls

python ./get_repo.py

call config.bat
ngrok config add-authtoken %authtoken%

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install gitpython



pause
exit