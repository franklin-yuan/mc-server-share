import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
import random
from git import Repo

print("Getting new files:")

repo = git.Repo(config.worldpath)
#print(repo.git.status())
print(repo.git.execute("git pull origin main"))

#repo.git.execute("git checkout -b my_branch")
