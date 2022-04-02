import time
import webbrowser
import tkinter as Tk
from tkinter import *
import requests
import webview


root = Tk()


# web stuff
def webv():
    webview.create_window(title='YouTube', url='https://www.youtube.com/')
    webview.start()
    



# Gui stuff
root.geometry('800x400')
root.resizable(FALSE, FALSE)
root.configure(bg='#252526')
root.option_add('*tearOff', FALSE)
root.title('WebApplication')

m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Web-Servers")
root['menu'] = m
m_edit.add_command(label="Youtube", command=webv)
m_edit.add_command(label="Twitch", command=print('http://www.twitch.com'))
m_edit.add_command(label="Steam", command=print('http://www.Steam.com'))
m_edit.add_command(label="Radio-Stations", command=print('http://streema.com/ , https://www.iheart.com/'))
m_edit.add_command(label="Exit", command=quit)
root.mainloop()


# URL's to Websites

#url = input('http://streema.com/')
#url1 = input('Webpage to grab source from: ')
#url2 = input('Webpage to grab source from: ')
#url3 = input('Webpage to grab source from: ')
#url4 = input('Webpage to grab source from: ')
#url5 = input('Webpage to grab source from: ')


#html_output_name = input('Name for html file: ')

#req = requests.get(url, 'html.parser')

#with open(html_output_name, 'w') as f:
#    f.write(req.text)
#    f.close()

#def Main():
#    global Main
#    global top
#    top = Toplevel()
#    top.geometry('800x400')
#    top.resizable(FALSE, FALSE)
#    button = Button(root, text="Play", command=Main).pack()
#root.mainloop()



# Set to Vm
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#venv\scripts\activate
