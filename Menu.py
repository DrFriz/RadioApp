from cProfile import label
from tkinter import *
from turtle import title


#  Import tkinter as tk
root = Tk()

#  Setting Menu Settings
root.geometry('800x400')
root.configure(bg='#252526')


root.option_add('*tearOff', FALSE)
root.title('Radio App')

#  Radio Menu Open Def
def open():
    top = Toplevel()
    top.geometry('800x400')
    top.configure(bg='#252526')
    










#  Menu Options
m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Options")
root['menu'] = m
m_edit.add_command(label="Radio Stations", command=open)
m_edit.add_command(label="Exit", command=quit)
m_edit.add_command(label="New Window")





root.mainloop()