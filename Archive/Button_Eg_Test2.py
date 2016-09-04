import tkinter as tk
from tkinter import ttk

norm_font = ('Calibri', 12)



def popupmsg():
    popup=tk.Tk()
    popup.wm_title ("Testing Function Call")
    label = ttk.Label(popup, text = button_test, font=norm_font)
    label.pack()
    B1 = ttk.Button (popup, text='Ok', command = popup.destroy)
    B1.pack()
    popup.mainloop()

#Button function is HERE!
def button_test():
    print (directory.get())
    

class ButtonTestPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title (self, 'File Transfer') #Window Title

        container = tk.Frame(self)	
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure (0, weight=1) 
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label = 'Button Test 2', command = lambda: popupmsg('Yay it worked'))
        menubar.add_cascade(label='File', menu=filemenu)

        tk.Tk.config(self,menu=menubar)

        self.frames = {} 


        for F in (StartPage, FirstPage):

            frame = F(container, self) 

            self.frames[F] = frame

            frame.grid (row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame= self.frames[cont]
        frame.tkraise()

# First Page, has button function that grabs input from entry field.

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_1 = ttk.Label (self, text='Directory Path')
        label_1.grid (row=2, column=1, columnspan=1)

        global directory
        directory = ttk.Entry(self)
        directory.grid(row=2, column=2, columnspan=1, sticky = 'e')
    #Button function is called here under command.

        submit = ttk.Button (self, text='Submit', command=button_test)
        submit.grid(row=6, column=2, pady = 15)
        

#Throw away page, as can't be bothered to change the framework.

class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label (self, text='Start Page')
        label.pack(pady=10, padx=10)

        label_1 = tk.Label (self, text='Directory Path')
        label_1.pack (pady=10, padx=10)

        
app = ButtonTestPage()
app.mainloop()
