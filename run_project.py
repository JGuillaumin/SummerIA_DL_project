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
os.system("ls -la /valohai/inputs/*")
time.sleep(1)
print("\n===============\n")

if os.path.isfile("main.py"):
    os.system("python main.py")
else:
    print("main.py not found")

if os.path.isfile("/valohai/inputs/main_script/main2.py"):
    os.system("python /valohai/inputs/main_script/main2.py")
else:
    print("/valohai/inputs/main_script/main2.py not found")