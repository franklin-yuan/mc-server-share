import os 
import config
os.environ["GIT_PYTHON_REFRESH"] = "quiet"


import git
import random
from git import Repo
import time

from pathlib import Path
folder_path = Path.cwd()
print(os.path.dirname(folder_path))
config.worldpath = os.path.dirname(folder_path)

print("Getting new files (takes a long time for the first time):")

repo = git.Repo(config.worldpath)
#print(repo.git.status())
print(repo.git.execute("git fetch --all"))
print(repo.git.execute("git reset --hard origin/main"))

# import ngrok

# session = ngrok.SessionBuilder.authtoken("20FlLRf2lwrf5bRSRSr4berWmMw_3cj7zPrVNjiPwbzf3ccaC")
# listener = ngrok.forward("localhost:8080", authtoken_from_env=True,
#     proto="tcp")

# print(f"Ingress established at: {listener.url()}");



print("Type 'stop' into this terminal when you want to end the server!")

time.sleep(1)

# import ngrok

# listener = ngrok.forward("localhost:8080",
#     proto="tcp")

# print(f"Ingress established at: {listener.url()}");

#repo.git.execute("git checkout -b my_branch")
