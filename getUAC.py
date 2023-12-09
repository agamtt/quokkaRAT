import os
import subprocess
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define the path to your Python script that you want to run with admin rights
script_path = r'open_calc.py'  # Replace with the actual path

# Check if the script file exists
if not os.path.isfile(script_path):
    print(f"Script not found: {script_path}")
    input() # pause script
    sys.exit(1)

# Define the command to run your Python script with 'runas' for admin rights
command = f'runas /user:Administrator "python {script_path}"'

try:
    subprocess.run(command, shell=True, check=True)
except Exception as e:
    print(f"Error: {e}")
else:
    print("Script executed with admin rights.")
