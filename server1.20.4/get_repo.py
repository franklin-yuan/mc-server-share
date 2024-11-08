
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

# dir_path = os.path.dirname(os.path.realpath(__file__))
# dir_path = os.path.join(dir_path, r"server1.20.4")
# if(os.path.exists(dir_path)):
#     # block of code
#     print()
# else:
#     print("assets not found!\ncheck your directory")

print("Initiating repository:")
time.sleep(1)

Repo.init(config.worldpath)

try:

    repo = git.Repo(config.worldpath)
    print(repo.git.status())
    print(repo.git.execute("git remote add origin https://github.com/franklin-yuan/mc-server-share.git"))
    print(repo.git.execute("git branch -M main"))
    #print(repo.git.execute("git config --global --type bool push.autoSetupRemote true"))
except:
    print("Something weird happened or repository already initiated")

print(r"""
             _
           /(_))
         _/   /
        //   /
       //   /
       /\__/
       \O_/=-.
   _  / || \  ^o
   \\/ ()_) \.
    ^^ <__> \()
      //||\\
     //_||_\\  ds
    // \||/ \\
   //   ||   \\
  \/    |/    \/
  /     |      \
 /      |       \
        |
      """)

print("We need your ngrok authentication token (authtoken) now. Please make sure you have signed up and have your authtoken ready.")
token = input("Authtoken: ")
token.replace(" ", "")
f = open("config.bat", "w+")
f.write("set authtoken="+token)
f.close()
import ngrok
ngrok.set_auth_token(token)


