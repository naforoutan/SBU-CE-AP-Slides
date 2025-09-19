import os
import subprocess
import sys

base_dir = os.getcwd()
python_exec = sys.executable

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".ipynb"):
            notebook_path = os.path.join(root, file)
            print(f"🔄 Converting: {notebook_path}")
            
            try:
                subprocess.run(
                    [
                        python_exec, "-m", "nbconvert",
                        "--to", "html",
                        "--embed-images",
                        notebook_path
                    ],
                    check=True
                )
                print(f"✅ Done: {notebook_path}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed: {notebook_path}")
                print(e)