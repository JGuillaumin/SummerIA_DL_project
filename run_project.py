import subprocess
import os
import time

#subprocess.call(["nvidia-smi"])
#subprocess.call(["ls", "-l"])
#subprocess.call(["nvidia-smi"])

print("\n===============\n")
os.system("nvidia-smi")
time.sleep(1)
print("\n===============\n")
os.system("ls -l")
time.sleep(1)
print("\n===============\n")
os.system("pwd")
time.sleep(1)
print("\n===============\n")
os.system("ls -la /valohai/*")
time.sleep(1)
print("\n===============\n")

if os.path.isfile("main.py"):
    os.system("python main.py")
else:
    print("main.py not found")

if os.path.isfile("main2.py"):
    os.system("python main2.py")
else:
    print("main2.py not found")