import os
import shutil
import time
os.chdir('C:\\') 


dir_src = ("C:\\Users\shell\Desktop\\New Customer Orders\\")
dir_dst = ("C:\\Users\shell\Desktop\\All Customer Orders\\")

currentTime = time.time()
modifiedTime = os.path.getmtime(dir_src)

for filename in os.listdir(dir_src):
    if filename.endswith('.txt') and currentTime - modifiedTime < 86400:
        shutil.move( dir_src + filename, dir_dst)
    print(filename)
