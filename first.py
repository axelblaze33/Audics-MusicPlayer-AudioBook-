from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from subprocess import call
import os

root = Tk()
root.geometry('600x400')
root.wm_title('Audics')

def control():
    os.system('application.py')
    #call(["Python3","application.py"])
btn = Button(root,
             text ="Load Songs",
             command = control)

btn.grid(column = 1,row = 1)

root.mainloop()

