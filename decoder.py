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
    newwin.geometry("250x250")
    newwin.config(bg="#282828")
    newwin.attributes("-alpha", 0.90)
    newwin.iconbitmap(link)
    scrollbar = Scrollbar(newwin)
    scrollbar.pack(side=RIGHT, fill=Y)
    messagebar=tk.Entry(newwin,bg="#282828",fg="white")
    messagebar.pack()
    mess=messagebar.get()
    enter=Button(newwin,text='Enter',command=MSG, font="Geneva 25 bold",activebackground="#282828",highlightbackground="#282828",activeforeground='black',fg='black')
    enter.pack()
    
    listbox = Listbox(newwin,)
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
    newwin2.geometry("250x100")
    newwin2.config(bg="#282828")
    newwin2.attributes("-alpha", 0.90)
    newwin2.iconbitmap(link)
    messagebar2=tk.Entry(newwin2,bg="#282828",fg="white")
    messagebar2.pack()
    enter1=Button(newwin2,bg='light grey',text='Enter',command=Decode, font="Geneva 25 bold",activebackground="#282828",highlightbackground="#282828",activeforeground='black',fg='black')
    enter1.pack()
    
    
def Decode():    
    enter=messagebar2.get()
    msg=str()
    for x in range(0,len(enter)-4):
        x=((x)*4)
        msg=((msg)+(enter[x]))
        endmsg=Label(newwin2,bg='light grey',text=(msg.strip()))
        endmsg.place(x=100,y=70)
            
def Exit():
    sys.exit()
                                                                         
root=Tk()
root.title("Decoder")
link=r'icon.ico'
root.iconbitmap(link)
root.geometry("380x200")
root.config(bg="#282828")
root.attributes("-alpha", 0.90)
title=tk.Label(root,text="Welcome to the Decoder",fg="white", font="Geneva 30 bold",bg="#282828")
title.pack()

write=Button(root,text="Writing message",command=NewwindM, font="Geneva 25 bold",highlightbackground="#282828",activeforeground='black',fg='white')
write.pack()

decode=Button(root,text="Decoder",command=NewwindD, font="Geneva 25 bold",highlightbackground="#282828",activeforeground='black',fg='white')
decode.pack()

exit=Button(root,text="Exit", command=Exit, font="Geneva 25 bold",highlightbackground="#282828",activeforeground='black',fg='white')
exit.pack()

root.mainloop()