import os
import shutil
from pathlib import Path
import getpass

def get(index=-1):
    username = getpass.getuser()
    target_dir = Path(f"C:/Users/{username}/leo_notebooks")
    source_dir = Path(__file__).resolve().parent.parent.parent / "notebooks"

    target_dir.mkdir(parents=True, exist_ok=True)

    for file in source_dir.glob("*.ipynb"):
        shutil.copy(file, target_dir)

    print(f"Jupyter notebooks copied to: {target_dir}")
