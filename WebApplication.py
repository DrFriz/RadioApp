from tkinter import *
from pytest import skip
import webview


root = Tk()

root.geometry('800x400')
root.configure(bg='#252526')
root.option_add('*tearOff', FALSE)
root.title('WebApps - Tkinter')
root.resizable(FALSE, FALSE)


      
def YouTube():
    webview.create_window(title='YouTube', url='https://www.YouTube.com/')
    webview.start()

def Twitch():
    webview.create_window(title='YouTube', url='https://www.Twitch.com/')
    webview.start()

def Steam():
    webview.create_window(title='YouTube', url='https://store.steampowered.com/')
    webview.start()

def Racer():
    webview.create_window(title='YouTube', url='https://www.Racer.com/')
    webview.start()



#  Drop Down Radio Menu
m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Web-Servers")
root['menu'] = m
m_edit.add_command(label="Youtube", command= YouTube)
m_edit.add_command(label="Twitch", command= Twitch)
m_edit.add_command(label="Steam", command= Steam)
m_edit.add_command(label="R-A-C-E-R-S", command= Racer)
m_edit.add_command(label="Exit", command=quit)






#def YT():
    #top = Toplevel()
    #top.geometry('800x400')
    #top.configure(bg='#252526')
    #top.option_add('*tearOff', FALSE)
    #top.title('YouTube - Tkinter')
    #top.resizable(FALSE, FALSE)
    #print

root.mainloop()







#  Radio Websites
#  https://streema.com/ , https://www.iheart.com/
