@echo off

echo Please select which world you would like to host. The current worlds include:
echo Current worlds include:
cd ..
git branch -r
echo Entering one that is not in the list will create a new world of that name.
set /p world=Enter world (without the 'origin/', etc main):

git checkout %world%

echo Currently on:

git branch

pause