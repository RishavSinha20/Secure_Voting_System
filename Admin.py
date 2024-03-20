import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from registerVoter import *
from admFunc import *


def AdminHome(root, frame1, frame3):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()

    # Button color
    button_bg = "#FF6347"  # Tomato
    button_fg = "#FFFFFF"  # White


    # Destroy previous button if it exists
    if hasattr(frame3, "home_button"):
        frame3.home_button.destroy()

    frame3.home_button = Button(frame3, text="Admin", command=lambda: AdminHome(root, frame1, frame3), font=('Times New Roman', 30), relief="raised", borderwidth=10,bg = "#FCCA46",fg = "#A4031F")
    frame3.home_button.pack(side=LEFT, padx=10, pady=10)

    Label(frame1, text="Admin", font=('Times New Roman', 50, 'bold'),  bg="#A1C181",fg="#233D4D").pack(pady=30)
    Label(frame1, text="",bg="#A1C181").pack()


    # Admin Login
    runServer = Button(frame1, text="Run Server", width=15, font=('Times New Roman', 20), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: sb_p.call('start python Server.py', shell=True))

    # Voter Login
    registerVoter = Button(frame1, text="Register Voter", width=15, font=('Times New Roman', 20), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: regV.Register(root, frame1))

    # Show Votes
    showVotes = Button(frame1, text="Show Votes", width=15, font=('Times New Roman', 20), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: adFunc.showVotes(root, frame1))



    Label(frame1, text="",bg="#A1C181").pack()
    runServer.pack()
    Label(frame1, text="",bg="#A1C181").pack()
    registerVoter.pack()
    Label(frame1, text="",bg="#A1C181").pack()
    showVotes.pack()

    frame1.pack()
    root.mainloop()


def log_admin(root, frame1, admin_ID, password):

    if(admin_ID == "Admin" and password == "admin"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect!!", width=500, font=('Times New Roman', 25), fg="#233D4D", bg="#A1C181")
        msg.pack()
        
def AdmLogin(root, frame1):
    root.title("Admin Login")

    for widget in frame1.winfo_children():
        widget.destroy()

    # Main title
    Label(frame1, text="Admin Login", font=('Times New Roman', 30, 'bold'), fg="#233D4D", bg="#A1C181").pack(pady=(50, 20))

    # Admin ID and Entry
    admin_frame = Frame(frame1, bg="#A1C181")
    admin_frame.pack(pady=10)
    Label(admin_frame, text="Admin ID:", font=('Times New Roman', 20), fg="#233D4D", bg="#A1C181").pack(side=LEFT, padx=20)
    admin_ID = tk.StringVar()
    Entry(admin_frame, textvariable=admin_ID, font=('Times New Roman', 20)).pack(side=LEFT)

    # Password and Entry
    password_frame = Frame(frame1, bg="#A1C181")
    password_frame.pack(pady=10)
    Label(password_frame, text="Password: ", font=('Times New Roman', 20), fg="#233D4D", bg="#A1C181").pack(side=LEFT, padx=20)
    password = tk.StringVar()
    Entry(password_frame, textvariable=password, show='*', font=('Times New Roman', 20)).pack(side=LEFT)

    # Login Button
    button_frame = Frame(frame1, bg="#A1C181")
    button_frame.pack(pady=20)
    Button(button_frame, text="Login", width=10, font=('Times New Roman', 20), bg="#FCCA46", fg="#A4031F" , relief="raised", borderwidth=10,command=lambda: log_admin(root, frame1, admin_ID.get(), password.get())).pack()

    # Centering everything
    frame1.pack(expand=True, fill="both")
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_rowconfigure(0, weight=1)

    root.mainloop()

'''
if _name_ == "_main_":
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    frame1 = Frame(root)
    frame3 = Frame(root)
    AdminHome(root,frame1,frame3)
    '''
#Admin