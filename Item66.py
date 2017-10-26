# Python 3.6.4
# Shelley Tennison
# Drill for the Tech Academy Python course.

import os
import shutil
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)
        self.varS=StringVar()
        self.varD=StringVar()
        #setting up the GUI in the parent frame
        self.master = master
        self.create_db()
        self.update()
        self.master.title('File Transfer SQLite3')
        self.master.configure(bg="#F0F0F0")
        self.master.rowconfigure(3, weight=1)
        self.grid(sticky=W+E+N+S)
        self.source = "Source"
        self.destination = "Destination"
        arg = self.master

        #buttons

        #Source
        self.src_button = Button(self, text="Select Source Folder", command=self.select_src, width=25)
        self.src_button.grid(row=1, column=0, sticky=W)  
        #Destination
        self.src_button = Button(self, text="Select Destination Folder", command=self.select_dst, width=25)
        self.src_button.grid(row=2, column=0, sticky=W)
        #copy button
        self.move_button = Button(self, text="Copy Files", command=self.copy_files, width=25)
        self.move_button.grid(row=3, column=0, sticky=W)

                       
    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
            self.master.destroy()
            os._exit(0)

                       
    def create_db(self):
        conn = sqlite3.connect('db_Item66.db')
        with conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS tbl_filecopy(ID INTEGER PRIMARY KEY AUTOINCREMENT,date TEXT,time TEXT,files_copied INT);")
            conn.commit()
        conn.close()

    def timestamp(self):
        conn = sqlite3.connect('db_Item66.db')
        with conn:
            c = conn.cursor()
            c,count = count_records(c)
            if count >= 1:
                c.execute("SELECT * FROM tbl_filecopy ORDER BY DESC LIMIT 1")
                last_timestamp = c.fetchall()
                last_timestamp_list = last_timestamp[0]
                last_date = last_timestamp_list[1]
                last_time_unix = last_timestamp_list[2]
                last_time = datetime.datetime.fromtimestamp(int(round(float(last_time_unix)))).strftime("%H:%M:%S")
                last_copies = str(last_timestamp_list[3])
                last_timestamp = ("This application was last run on, "+last_date+" at "+last_time_unix+" and "+last_copies+" were copied.")
                print(last_timestamp)
            else:
                print("This program has not been run before.")
        conn.close()

    def count_records(c):
        count = ""
        c.execute("SELECT COUNT(*) FROM tbl_filecopy")
        count = c.fetchone()[0]
        return c,count

    def add_timestamp(self):
        conn = sqlite3.connect('db_Item66.db')
        with conn:
            c = conn.cursor()
            c.execute("INSERT INTO tbl_filecopy (date,time,files_copied) VALUES (?,?,?)",(date,local_time,files_copied))
            conn.commit()
        conn.close()    

    def update(self):
        #Label of last move
        self.timestamp_lbl = Label(self, text="")
        self.timestamp_lbl.grid(row=0, column=0, sticky=W, padx = 10, pady = 10)
        #Get last move date
        conn=sqlite3.connect("db_Item66.db")
        c = conn.cursor()
        c.execute("SELECT date FROM tbl_filecopy ORDER BY date DESC LIMIT 1")
        last_run = c.fetchone()
        if last_run == None:
            self.timestamp_lbl.config(text="No previous files have been moved.")
        else:
            self.timestamp_lbl.config(text=last_run[0])

    def select_src(self):
        desName = filedialog.askdirectory()
        self.varS.set(desName)
        

    def select_dst(self):
        desName = filedialog.askdirectory()
        self.varD.set(desName)

    def copy_files(self):
        global local_time
        local_time = time.time()
        global date
        date = time.strftime("%d/%m/%Y")
        source = self.varS.get()
        destination = self.varD.get()
        source_files = len(os.listdir(destination))
        for i in os.listdir(source):
            time_file = os.path.getmtime(source)
            if local_time - 86400 <= time_file:
                shutil.copy(source+i,destination)
                add_timestamp(self)
        destination_files = len(os.listdir(source))
        global files_copied
        files_copied = destination_files - source_files
        if files_copied > 0:
            print("Files successfully copied.")
        else:
            print("There are no files to copy.")
        




if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
