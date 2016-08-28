import tkinter as tk
from tkinter import ttk
import shutil, os

#Sorting Algorithm

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

def MoveFile():
    for L in F:
        S.append(L)

    bubble(S)

    n = 17
    for i in S:
        if n<10:
            name = +str(n)+'.mp4'
        else:
            name = 'Girl Meets World S02E'+str(n)+'.mp4'
        shutil.copy (str(source) + '\\' + str(i), newloc +'\\' + name)
        os.unlink(source + '\\' + i)
        print ('file' + str(n))
        n+=1

#def buttonSubmit():
    
    

########
##GUI##
########

LARGE_FONT = ('Calibri', 12)
FONT = ('Calibri', 10)

    
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
        
        label = ttk.Label (self, text='Start Page', font=LARGE_FONT)
        label.grid(row= 1, column=1, pady=10, padx=10)

        label_1 = ttk.Label (self, text='Directory Path', font=FONT)
        label_1.grid (row=2, column=1, columnspan=1)

        directory = ttk.Entry(self)
        directory.grid(row=2, column=2, columnspan=1)

        newLocation_Label = ttk.Label (self, text='New Location', font=FONT)
        newLocation_Label.grid (row=3, column=1, columnspan=1, padx=5, pady=5)

        newLocation = ttk.Entry(self)
        newLocation.grid(row=3, column=2, columnspan=1, padx=5, pady=5)

        newName_Label = ttk.Label (self, text='New Name', font=FONT)
        newName_Label.grid (row=4, column=1, columnspan=1, padx=5, pady=5)

        newName = ttk.Entry(self)
        newName.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

        fileExtension_Label = ttk.Label (self, text='File Extension', font=FONT)
        fileExtension_Label.grid (row=5, column=1, columnspan=1)
        
        fileExtension = ttk.Entry(self)
        fileExtension.grid(row=5, column=2, columnspan=2)

        submit = ttk.Button (self, text='Submit', command=MoveFile)
        submit.grid(row=6, column=2, pady = 15)
        

class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label (self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_1 = tk.Label (self, text='Directory Path', font=FONT)
        label_1.pack (pady=10, padx=10)

def MoveFile():
    source = directory.get()
    newloc = newLocation.get()

    F = os.listdir(source1)
    S=[]

    for L in F:
        S.append(L)

    bubble(S)

    n = 1
    for i in S:
        if n<10:
            name = newName[:-1] +str(n)+ fileExtension
        else:
            name = newName[:-1] +str(n)+ fileExtension
        shutil.copy (str(source) + '\\' + str(i), newloc +'\\' + name)
        os.unlink(source + '\\' + i)
        print ('file' + str(n))
        n+=1


app = FileTransfer()
app.mainloop()