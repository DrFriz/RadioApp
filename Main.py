from cProfile import label
#from signal import pause
from tkinter import *
from turtle import title
from tkinter import ttk
import webbrowser
import vlc
import os
import time
import pafy
import youtube_dl

#os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')



#  Import tkinter as tk
root = Tk()

#  Setting Menu Settings
root.geometry('800x400')
root.resizable(FALSE, FALSE)
root.attributes("-alpha", 0.99)
root.attributes("")
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
    global top1
    top1 = Toplevel()
    top1.title('Drawing Menu')
    top1.geometry('800x400')
    top1.resizable(FALSE, FALSE)
    top1.configure(bg='')
    buttonUrl = Button(top1, text="Play", command=playSound).pack()
    #buttonUr2 = Button(top1, text="Pause", command=player.pause()).pack()
    #buttonUrl = Button(top1, text="Play", command=playSound).pack()


def playSound():

    global playSound
    url = 'https://www.youtube.com/watch?v=Qs-8xYwYJAQ&list=PLMItTFx19QcH1YUvkdV1q1ZnK9NaQBYqk'
    
    song = pafy.new(url)
    duration = song.length
    audiostreams = song.audiostreams
    best = song.getbest()
    play_url = best.url
    
    print(play_url)

    instance = vlc.Instance('--no-video')

    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()
    player.set_media(media)
    player.play()
    #player.pause()

    #time.sleep(duration)


#  Menu Options
m = Menu(root)
m_edit = Menu(m)
m.add_cascade(menu=m_edit, label="Options")
root['menu'] = m
m_edit.add_command(label="Radio Stations", command=RadioMenu)
m_edit.add_command(label="Drawing Window", command=DrawingMenu)
m_edit.add_command(label="Exit", command=quit)





#url = 'https://www.youtube.com/watch?v=Qs-8xYwYJAQ&list=PLMItTFx19QcH1YUvkdV1q1ZnK9NaQBYqk'

#song = pafy.new(url)
#duration = song.length
#audiostreams = song.audiostreams
#best = song.getbest()
#play_url = best.url

#print(play_url)

#instance = vlc.Instance('--no-video')

#player = instance.media_player_new()
#media = instance.media_new(play_url)
#media.get_mrl()
#player.set_media(media)


#time.sleep(duration)







root.mainloop()

#  http://streema.com/radios/play/96.3_Jack_FM https://www.iheart.com/live/963-jack-fm-9150/