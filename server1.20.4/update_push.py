import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
import random
from git import Repo

from pathlib import Path

folder_path = Path.cwd()
print(os.path.dirname(folder_path))
config.worldpath = os.path.dirname(folder_path)

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

print("Wait until this terminal says 'complete'")
print(repo.git.execute("git push -u origin "+config.current_branch))
print("Complete")
import time
time.sleep(1)
print(r"""
                   YAao,
                    Y8888b,
                  ,oA8888888b,
            ,aaad8888888888888888bo,
         ,d888888888888888888888888888b,
       ,888888888888888888888888888888888b,
      d8888888888888888888888888888888888888,
     d888888888888888888888888888888888888888b
    d888888P'                    `Y888888888888,
    88888P'                    Ybaaaa8888888888l
   a8888'                      `Y8888P' `V888888
 d8888888a                                `Y8888
AY/'' `\Y8b                                 ``Y8b
Y'      `YP                                    ~~
         `'
""")
#repo.git.execute("git checkout -b my_branch")

