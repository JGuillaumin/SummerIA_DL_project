import subprocess
import os

subprocess.call(["nvidia-smi"])
subprocess.call(["ls", "-l"])
subprocess.call(["nvidia-smi"])

if os.path.isfile("main.py"):
    os.system("main.py")
else:
    print("main.py not found")