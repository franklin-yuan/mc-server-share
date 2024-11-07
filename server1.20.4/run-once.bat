@echo off


:start
cls

python ./get_repo.py
python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install gitpython



pause
exit