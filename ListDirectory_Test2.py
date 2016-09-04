#Directory List GUI Test

#Just to test 1st stage that it is able ot grab a list of the directory GUI is copy
#of the basic GUI set up and first window.

import tkinter as tk
from tkinter import ttk
import os

# ListDirectory Pop Up Window

def listDir():
    someList=[]
    folder = os.listdir(directory.get())
    for F in folder:
        someList.append(F)
    return someList

def popupWin():
    popup=tk.Tk()
    popup.wm_title ("Testing Function Call")
    label = ttk.Label(popup, text ='\n'.join(map(str, listDir())), font=FONT)
    label.pack()
    B1 = ttk.Button (popup, text='Ok', command = popup.destroy)
    B1.pack()
    popup.mainloop()

    #tk.messagebox.showinfo('Welcome', 'Please ' + str(listDir()))
  
    

FONT = ('Times New Roman', 12)
LARGE_FONT = ('Calibri', 12)



##Button Command##    

class FileTransfer(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title (self, 'File Transfer') #Window Title

        container = tk.Frame(self)	
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure (0, weight=1) 
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} 


        for F in (StartPage, FirstPage):

            frame = F(container, self) 

            self.frames[F] = frame

            frame.grid (row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame= self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)        
            
        label = ttk.Label (self, text='Start Page', font=FONT)
        label.grid(row= 1, column=1, pady=10, padx=10)

        directory_Label = ttk.Label (self, text='Directory Path', font=FONT)
        directory_Label.grid (row=2, column=1, columnspan=1)

        global directory
        directory = ttk.Entry(self)
        directory.grid(row=2, column=2, columnspan=2)


        submit = ttk.Button (self, text='Submit', command=popupWin)
        submit.grid(row=6, column=2, pady = 15)

class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label (self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = tk.Label (self, text='Directory Path', font=FONT)
        label_1.pack (pady=10, padx=10)



app = FileTransfer()
app.mainloop()
