
import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"

import git
import random
from git import Repo

from pathlib import Path
folder_path = Path.cwd()
print(folder_path)

config.worldpath = folder_path

# dir_path = os.path.dirname(os.path.realpath(__file__))
# dir_path = os.path.join(dir_path, r"server1.20.4")
# if(os.path.exists(dir_path)):
#     # block of code
#     print()
# else:
#     print("assets not found!\ncheck your directory")

print("Fetching files:")

Repo.init(config.worldpath)

repo = git.Repo(config.worldpath)
print(repo.git.status())
print(repo.git.execute("git remote add origin https://github.com/franklin-yuan/mc-server-share.git"))
print(repo.git.execute("git branch -M main"))
#print(repo.git.execute("git config --global --type bool push.autoSetupRemote true"))

