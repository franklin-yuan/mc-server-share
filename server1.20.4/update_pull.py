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

print("Getting new files:")

repo = git.Repo(config.worldpath)
#print(repo.git.status())
print(repo.git.execute("git fetch --all"))
print(repo.git.execute("git reset --hard origin/main"))


#repo.git.execute("git checkout -b my_branch")
