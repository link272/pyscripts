import os
import subprocess
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        name = os.path.join(root, name)[2:]
        if ".cbr" in name:
            print(name[:-3])
            subprocess.check_call(["mkdir", "tmp"])
            subprocess.check_call(["unrar", "x", name, "./tmp/"])
            subprocess.check_call(["convert", "./tmp/*.jpg", name[:-3]+"pdf"])
            subprocess.check_call(["rm", "-R", "./tmp/"])
            print(name[:-3])
        if ".cbz" in name:
            print(name[:-3])
            subprocess.check_call(["mkdir", "tmp"])
            subprocess.check_call(["unzip", name, "-d","./tmp/"])
            input("Enter")
            subprocess.check_call(["convert", "./tmp/*.jpg", name[:-3]+"pdf"])
            subprocess.check_call(["rm", "-R", "./tmp/"])
            print(name[:-3])
print("done")