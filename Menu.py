from cProfile import label
from tkinter import *
from turtle import title
from tkinter import ttk


#  Import tkinter as tk
root = Tk()

#  Setting Menu Settings
root.geometry('800x400')
root.resizable(FALSE, FALSE)
root.attributes("-alpha", 0.99)
root.configure(bg='#252526')


root.option_add('*tearOff', FALSE)
root.title('Radio App')

#  Radio Menu Open Def
def RadioMenu():
    top = Toplevel()
    top.title('Radio Menu')
    top.geometry('800x400')
    top.resizable(FALSE, FALSE)
    top.configure(bg='#252526')

def DrawingMenu():
    top1 = Toplevel()
    top1.title('Drawing Menu')
    top1.geometry('800x400')
    top1.resizable(FALSE, FALSE)
    top1.configure(bg='')






#  Menu Options
m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Options")
root['menu'] = m
m_edit.add_command(label="Radio Stations", command=RadioMenu)
m_edit.add_command(label="Drawing Window", command=DrawingMenu)
m_edit.add_command(label="Exit", command=quit)





root.mainloop()