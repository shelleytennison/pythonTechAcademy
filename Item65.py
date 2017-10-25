# Shelley Tennison
# Drill for the Tech Academy Python Course. 


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import *
import os
import shutil
import datetime as dt
import time




#functions to attach in buttons

class gui:
    def __init__(self, *args, **kwargs):
        self.varS=StringVar()
        self.varD=StringVar()

        #Buttons & Labels
        self.browseButton = ttk.Button(text = "SourceFile  Folder", command = self.askSource).grid(row = 1, column = 2, padx = 5, pady = 5)
        self.browseButton = ttk.Button(text = "Destination Folder", command = self.askDestination).grid(row = 2, column = 2, padx = 5, pady = 5)       
        self.copyButton = ttk.Button(text = "Copy The Files", command = self.fileCopy).grid(row = 3, column = 1, padx = 5, pady = 5)
        self.pathLabel = ttk.Entry(text = self.varS).grid(row = 1, column = 1, padx = 1, pady = 1)
        self.pathLabel = ttk.Entry(text = self.varD).grid(row = 2, column = 1, padx = 1, pady = 1) 
        

    def askSource(self):
        desName=filedialog.askdirectory()
        self.varS.set(desName)

    def askDestination(self):
        desName=filedialog.askdirectory()
        self.varD.set(desName)

    def fileCopy(self):
        now=dt.datetime.now()
        
    
    #get the paths for send and recieving folders
        sender= self.varS.get()
        receiver= self.varD.get()
        ago=now-dt.timedelta(hours=24)
        for files in os.listdir(sender):
            path=os.path.join(sender, files)
            st=os.stat(path)
            mtime=dt.datetime.fromtimestamp(st.st_mtime)
            if mtime>ago:
                shutil.copy2(path, receiver)
                print (files)
            else:
                print ("There are no files to copy")
           


if __name__ =="__main__":
    root=Tk()
    gui=gui(root)
    root.mainloop()
