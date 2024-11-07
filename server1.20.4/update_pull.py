import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
import random
from git import Repo

print("Getting new files:")

repo = git.Repo(config.worldpath)
#print(repo.git.status())
print(repo.git.execute("git clone https://github.com/franklin-yuan/mc-server-share.git"))

#repo.git.execute("git checkout -b my_branch")
