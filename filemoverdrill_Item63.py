import os
import shutil
os.chdir('C:\\') 

dir_src = ("C:\\Users\shell\Desktop\\Folder A\\")
dir_dst = ("C:\\Users\shell\Desktop\\Folder B\\")

for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.move( dir_src + filename, dir_dst)
    print(filename)
