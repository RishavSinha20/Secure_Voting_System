#register voter
import tkinter as tk
from tkinter import ttk
from tkinter import *


from dframe import *
import dframe as df
from Admin import *

def reg_server(root, frame1, name, sex, zone, city, passw):
    if passw == '' or passw == ' ':
        msg = Message(frame1, text="               Error: Missing Fields", width=500,bg="#A1C181", fg="#233D4D",font=('Times New Roman', 20))
        msg.grid(row=19, column=0, columnspan=5)
        return -1

    vid = df.taking_data_voter(name, sex, zone, city, passw)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "\n\n\n\nRegistered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Times New Roman', 30), bg="#A1C181", fg="#233D4D").grid(row=19, column=0, columnspan=5)




def Register(root, frame1):
    root.title("Register Voter")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Set window background color
    root.configure(bg="#A1C181")  
    for widget in frame1.winfo_children():
        widget.destroy()


    Label(frame1, text="Register Voter                      ", font=('Times New Roman', 30,'bold'), bg="#A1C181", fg="#233D4D").grid(row=1, column=2, rowspan=1)
    Label(frame1, text="",bg="#A1C181").grid(row=0, column=0)

    # Labels with Moccasin background
    Label(frame1, text="",bg="#A1C181").grid(row=2, column=0)
    Label(frame1, text="",bg="#A1C181").grid(row=3, column=0)
    Label(frame1, text="",bg="#A1C181").grid(row=4, column=0)
    Label(frame1, text="Name:         ", anchor="e", justify=LEFT, bg="#A1C181", fg="#233D4D",font=('Times New Roman', 20,'bold')).grid(row=5, column=1)
    Label(frame1, text="",bg="#A1C181").grid(row =6,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row=7, column=0)
    Label(frame1, text=" Sex:              ", anchor="e", justify=LEFT, bg="#A1C181",fg="#233D4D", font=('Times New Roman', 20,'bold')).grid(row=8, column=1)
    Label(frame1, text="",bg="#A1C181").grid(row = 9,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row=10, column=0)
    Label(frame1, text=" Zone:           ", anchor="e", justify=LEFT, bg="#A1C181",fg="#233D4D", font=('Times New Roman', 20,'bold')).grid(row=11, column=1)
    Label(frame1, text="",bg="#A1C181").grid(row = 12,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row=13, column=0)
    Label(frame1, text=" City:             ", anchor="e", justify=LEFT, bg="#A1C181",fg="#233D4D", font=('Times New Roman', 20,'bold')).grid(row=14, column=1)
    Label(frame1, text="",bg="#A1C181").grid(row = 15,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row=16, column=0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT, bg="#A1C181",fg="#233D4D", font=('Times New Roman', 20,'bold')).grid(row=17, column=1)

    name = tk.StringVar()
    sex = tk.StringVar()
    zone = tk.StringVar()
    city = tk.StringVar()
    password = tk.StringVar()

    e2 = Entry(frame1, textvariable=name,width=20,font=('Times New Roman', 20)).grid(row=5, column=2)
    e5 = Entry(frame1, textvariable=zone,width=20,font=('Times New Roman', 20)).grid(row=11, column=2)
    e6 = Entry(frame1, textvariable=city,width=20,font=('Times New Roman', 20)).grid(row=14, column=2)
    e7 = Entry(frame1, textvariable=password,width=20,font=('Times New Roman', 20)).grid(row=17, column=2)

    e4 = ttk.Combobox(frame1, textvariable=sex, width=22,font=('Times New Roman', 18))
    e4['values'] = ("Male", "Female", "Transgender")
    e4.grid(row=8, column=2)
    e4.current()


    Label(frame1, text="",bg="#A1C181").grid(row=18, column=2)
   
    Label(frame1, text="",bg="#A1C181").grid(row = 20,column = 2)
    Label(frame1, text="",bg="#A1C181").grid(row = 21,column = 2)
    reg = Button(frame1, text="Register!",font=('Times New Roman', 22), relief="raised", borderwidth=10, bg="#FCCA46", fg="#A4031F", command=lambda: reg_server(root, frame1, name.get(), sex.get(), zone.get(), city.get(), password.get()),width=20)
    reg.grid(row=22, column=2,columnspan=2)

    frame1.pack(expand=True, fill="both")
    root.update_idletasks()
    frame1.place(in_=root, anchor="c", relx=.5, rely=.5)
    root.mainloop()

'''
if _name_ == "_main_":
    root = tk.Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Full screen
    # Set window background color to match frame background color
    frame_bg = "#FFE4B5"  # Moccasin
    root.config(bg=frame_bg)
    
    frame1 = Frame(root)
    Register(root, frame1)
'''