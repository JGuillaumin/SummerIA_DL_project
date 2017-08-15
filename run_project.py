import subprocess
import os
import time

#subprocess.call(["nvidia-smi"])
#subprocess.call(["ls", "-l"])
#subprocess.call(["nvidia-smi"])

print("\n===============\n")
os.system("nvidia-smi")
time.sleep(3)
print("\n===============\n")
os.system("ls -l")
time.sleep(3)
print("\n===============\n")
os.system("pwd")
time.sleep(3)
print("\n===============\n")


if os.path.isfile("main.py"):
    os.system("main.py")
else:
    print("main.py not found")


if os.path.isfile("main2.py"):
    os.system("main2.py")
else:
    print("main.py not found")