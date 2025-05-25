import subprocess
try:
    subprocess.Popen(r"Window\pythonUE.exe")
    subprocess.Popen(r"dist\temp\server.exe")
except:
    print("File not found")
