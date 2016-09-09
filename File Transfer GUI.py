#! python3

import tkinter as tk
from tkinter import ttk
import os, shutil
from send2trash import *

##Sort Function##

def Recycle():
    send2trash(directory.get())
    popup=tk.Tk()
    popup.wm_title ("Folder Deleted")
    label = ttk.Label(popup, text ='Folder Deleted!', font=LARGE_FONT)
    label.pack()
    B1 = ttk.Button (popup, text='Ok', command = popup.destroy)
    B1.pack()
    

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

##File Transfer Function##

def File_Transfer():
    folder = os.listdir(directory.get())
    source = directory.get()
    newFolder = newLocation.get()
    fileName = newName.get()
    extn = fileExtension.get()

    S = []
    for L in folder:
        S.append(L)
    bubble(S)

    n = 1
    for i in S:
        if n < 10:
            name = fileName[:-1]+str(n) + '.' + str(extn)
        else:
            name = fileName[:-2]+str(n) + '.' + str(extn)

        shutil.copy (str(source) + '\\' + str(i), newFolder + '\\' + name)
        n += 1

    popup=tk.Tk()
    popup.wm_title ("Complete!")
    label = ttk.Label(popup, text ='File transfer complete.', font=LARGE_FONT)
    label.pack()
    B1 = ttk.Button (popup, text='Ok', command = popup.destroy)
    B1.pack()
    B2 = ttk.Button (popup, text='Delete Folder', command = Recycle)
    B2.pack()
    popup.mainloop()

def File_Rename():
    folder = os.listdir(directory.get())
    source = directory.get()
    fileName = newName.get()
    extn = fileExtension.get()

    S = []
    for L in folder:
        S.append(L)
    bubble(S)

    n = 1
    for i in S:
        if n < 10:
            name = fileName[:-1]+str(n) + '.' + str(extn)
        else:
            name = fileName[:-2]+str(n) + '.' + str(extn)

        os.replace(str(source) +'\\'+ i, str(source) +'\\' + str(name))
        n += 1
    

    popup=tk.Tk()
    popup.wm_title ("Complete!")
    label = ttk.Label(popup, text ='All Files Renamed.', font=LARGE_FONT)
    label.pack()
    B1 = ttk.Button (popup, text='Ok', command = popup.destroy)
    B1.pack()
    popup.mainloop()

#######GUI########
####Class Framework####
FONT = ('Calibri', 10)
LARGE_FONT = ('Calibri', 12)

class FileTransfer(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title (self, 'File Transfer') #Window Title

        container = tk.Frame(self)	
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure (0, weight=1) 
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} 

        frame = StartPage (container, self)

        self.frames[StartPage] = frame

        frame.grid (row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame= self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
            
        label = ttk.Label (self, text='Start Page', font=LARGE_FONT)
        label.grid(row= 1, column=1, pady=10, padx=10)

        directory_Label = ttk.Label (self, text='Directory Path', font=FONT)
        directory_Label.grid (row=2, column=1, columnspan=1)

        global directory
        directory = ttk.Entry(self)
        directory.grid(row=2, column=2, columnspan=2)

        newLocation_Label = ttk.Label (self, text='New Location', font=FONT)
        newLocation_Label.grid (row=3, column=1, columnspan=1, padx=5, pady=5)

        global newLocation
        newLocation = ttk.Entry(self)
        newLocation.grid(row=3, column=2, columnspan=1, padx=5, pady=5)

        newName_Label = ttk.Label (self, text='New Name', font=FONT)
        newName_Label.grid (row=4, column=1, columnspan=1, padx=5, pady=5)

        global newName
        newName = ttk.Entry(self)
        newName.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

        fileExtension_Label = ttk.Label (self, text='File Extension', font=FONT)
        fileExtension_Label.grid (row=5, column=1, columnspan=1)

        global fileExtension
        fileExtension = ttk.Entry(self)
        fileExtension.grid(row=5, column=2, columnspan=2)

        rename = ttk.Button (self, text='Rename', command = File_Rename)
        rename.grid(row=6, column=2, pady = 3)

        transfer = ttk.Button (self, text='Transfer', command = File_Transfer)
        transfer.grid(row=7, column=2, pady = 3)

app = FileTransfer()
app.mainloop()
