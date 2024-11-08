import os
from pathlib import Path
folder_path = Path.cwd()
print(folder_path)
print(os.path.dirname(folder_path))