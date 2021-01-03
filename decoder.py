#######################################
#  code writen by
#                 Martin Gurasvili
#  licence: free to use and edit 
#######################################

import tkinter
import tkinter as tk
from tkinter import *
import random

def NewwindM():
    global messagebar
    global newwin
    global listbox
    newwin=tk.Toplevel(root)
    newwin.geometry("180x220")
    newwin.iconbitmap(link)
    messagebar=tk.Entry(newwin,bg='light grey')
    messagebar.pack()
    mess=messagebar.get()
    enter=Button(newwin,bg='light grey',text='Enter',command=MSG)
    enter.pack()
    scrollbar = Scrollbar(newwin)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(newwin)
    listbox.pack()
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    

def MSG():
    global listbox
    enc=["fdg","asd","wad","ads","ase","hfd","ere","yrh","sea"]
    
    mess=messagebar.get()
    msg=''
    
    for index in range(0,len(mess)):
        ran=random.randint(0,8)
        msg=((msg)+((mess[index])+(enc[ran])))

    endmsg=listbox.insert(END,msg)

def NewwindD():
    global newwin2
    global messagebar2
    newwin2=tk.Toplevel(root)
    newwin2.geometry("300x70")
    newwin2.iconbitmap(link)
    messagebar2=tk.Entry(newwin2,bg='light grey')
    messagebar2.pack()
    enter1=Button(newwin2,bg='light grey',text='Enter',command=Decode)
    enter1.pack()
    
    
def Decode():    
    enter=messagebar2.get()
    msg=str()
    for x in range(0,len(enter)-4):
        x=((x)*4)
        msg=((msg)+(enter[x]))
        endmsg=Label(newwin2,bg='light grey',text=(msg.strip()))
        endmsg.place(x=70,y=50)
            
def Exit():
    sys.exit()
                                                                         
root=Tk()
root.title("Decoder")
link=r'icon.ico'
root.iconbitmap(link)
root.geometry("250x100")
title=tk.Label(root,bg='light grey',text="Welcome to the Decoder")
title.pack()

write=Button(root,bg='light grey',text="Writing message",command=NewwindM)
write.pack()

decode=Button(root,bg='light grey',text="Decoder",command=NewwindD)
decode.pack()

exit=Button(root,bg='light grey',text="Exit", command=Exit)
exit.pack()

root.mainloop()