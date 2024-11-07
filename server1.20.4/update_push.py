import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
import random
from git import Repo

print("Upping files:")
user = input("What is your name: ")
try:
    print("Setting everything up... The first time could take a while")

    repo = git.Repo(config.worldpath)
    print(repo.git.status())
    print(repo.git.add("."))
    print(repo.git.status())

    print("Files added to commit")
    print(repo.git.commit(m="Update from "+user, ))
except:
    print("Something weird happened")

repo.git.autoset
print(repo.git.execute("git push -u origin main"))
print("Complete")
import time
time.sleep(1)
#repo.git.execute("git checkout -b my_branch")

