import subprocess as sb_p
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Admin import AdmLogin
from voter import voterLogin

def Home(root, frame1, frame2):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    # Button color
    button_bg = "#FCCA46"  # Gold
    button_fg = "#A4031F"  # Maroon

    Button(frame2, text="Home", command=lambda: Home(root, frame1, frame2), font=('Times New Roman', 30), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg).pack(side=LEFT, padx=10, pady=10)
    frame2.pack(side=TOP, fill=X)

    root.title("Home")

    # Frame color
    frame_bg = "#A1C181"  # light green

    frame1.config(bg=frame_bg)
    frame2.config(bg=frame_bg)  # Update frame2 background color

    Label(frame1, text="Home", font=('Times New Roman', 50), anchor='center', bg=frame_bg,fg="#233D4D").pack(pady=30)

    # Button colors
    button_bg = "#FF6347"  # Tomato
    button_fg = "#FFFFFF"  # White

    # Admin Login
    admin = Button(frame1, text="Admin Login", width=15, font=('Times New Roman', 30), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: AdmLogin(root, frame1))

    # Voter Login
    voter = Button(frame1, text="Voter Login", width=15, font=('Times New Roman', 30), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: voterLogin(root, frame1))

    # New Tab
    newTab = Button(frame1, text="New Window", width=15, font=('Times New Roman', 30), relief="raised", borderwidth=10, bg=button_bg, fg=button_fg, command=lambda: sb_p.call('start python homePage.py', shell=True))

    Label(frame1, text="", bg=frame_bg).pack()
    admin.pack()
    Label(frame1, text="", bg=frame_bg).pack()
    voter.pack()
    Label(frame1, text="", bg=frame_bg).pack()
    newTab.pack()

    frame1.pack(fill=BOTH, expand=True)
    root.mainloop()

def new_home():
    root = tk.Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Full screen
    frame1 = Frame(root)
    frame2 = Frame(root)
    
    # Set window background color to match frame background color
    frame_bg = "#A1C181"  #light green
    root.config(bg=frame_bg)
    
    Home(root, frame1, frame2)
    root.mainloop()

if __name__ == "__main__":
    new_home()