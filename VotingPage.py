#voting page
import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Times New Roman', 30, 'bold'),bg="#A1C181",fg="#233D4D").grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Times New Roman', 30, 'bold'),bg="#A1C181",fg="#233D4D").grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):
    
    # Button color
    button_bg = "#FCCA46"  # Gold
    button_fg = "#A4031F"  # Maroon
    
    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    frame_bg = "#A1C181"  #light green

    frame1.config(bg=frame_bg)

    Label(frame1, text="Cast Vote",bg="#A1C181",fg="#233D4D", font=('Times New Roman', 30, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#A1C181").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\nNarendra Modi", font=("Times New Roman",12, 'bold'),variable = vote, value = "bjp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"bjp",client_socket),relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).grid(row = 5,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,45)))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 5,column = 0)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 6,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 7,column = 0)
    
    Radiobutton(frame1, text = "Congress\nRahul Gandhi", font=("Times New Roman",12, 'bold'),variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket),relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).grid(row = 8,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((35,48)))
    congImg = Label(frame1, image=congLogo).grid(row = 8,column = 0)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 9,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 10,column = 0)
    
    Radiobutton(frame1, text = "Aam Aadmi Party\nArvind Kejriwal", font=("Times New Roman",12, 'bold'),variable = vote, value = "aap", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"aap",client_socket),relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).grid(row =11,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((55,40)))
    aapImg = Label(frame1, image=aapLogo).grid(row = 11,column = 0)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 12,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 13,column = 0)
    
    Radiobutton(frame1, text = "Shiv Sena\nUddhav Thackeray", font=("Times New Roman",12, 'bold'),variable = vote, value = "ss", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"ss",client_socket),relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).grid(row = 14,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((50,45)))
    ssImg = Label(frame1, image=ssLogo).grid(row = 14,column = 0)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 15,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 16,column = 0)
    
    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote,font=("Times New Roman",12, 'bold'), value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket),relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).grid(row = 17,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((45,35)))
    notaImg = Label(frame1, image=notaLogo).grid(row = 17,column = 0)

    frame1.pack()
    root.mainloop()

'''
if _name_ == "_main_":
        root = Tk()
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.configure(bg="#A1C181")
        frame1 = Frame(root)
        client_socket='Fail'
        votingPg(root,frame1,client_socket)
'''