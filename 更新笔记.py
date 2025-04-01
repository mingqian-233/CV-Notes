import subprocess
import os

# Define the paths to the scripts and their working directories
scripts = [
    {"path": "./images/download.py", "cwd": "./images"},
    {"path": "./notes/add_bg.py", "cwd": "./notes"},
    {"path": "./add_concept.py", "cwd": "."}
]

# Execute each script in order
for script in scripts:
    try:
        script_path = os.path.abspath(script["path"])
        script_cwd = os.path.abspath(script["cwd"])
        print(f"Running {script_path} in {script_cwd}...")
        subprocess.run(["python", script_path], check=True, cwd=script_cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_path}: {e}")
        break
