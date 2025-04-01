import subprocess

# Define the paths to the scripts
scripts = [
    "./images/download.py",
    "./notes/add_bg.py",
    "./add_concept.py"
]

# Execute each script in order
for script in scripts:
    try:
        print(f"Running {script}...")
        subprocess.run(["python", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script}: {e}")
        break
