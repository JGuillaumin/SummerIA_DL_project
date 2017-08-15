import subprocess
import os

#subprocess.call(["nvidia-smi"])
#subprocess.call(["ls", "-l"])
#subprocess.call(["nvidia-smi"])

print("\n===============\n")
os.system("nvidia-smi")
print("\n===============\n")
os.system("ls -l")
print("\n===============\n")
os.system("pwd")
print("\n===============\n")


if os.path.isfile("main.py"):
    os.system("main.py")
else:
    print("main.py not found")


if os.path.isfile("main2.py"):
    os.system("main2.py")
else:
    print("main.py not found")