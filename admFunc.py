#admFunc
import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()
    
    frame_bg = "#A1C181"  # light green
    frame1.config(bg=frame_bg)

    Label(frame1, text="Vote Count\n", font=('Times New Roman',40, 'bold'),fg="#233D4D",bg=frame_bg).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#A1C181").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35)))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)
    
    Label(frame1, text="BJP:                     ", font=('Times New Roman',30, 'bold'),bg=frame_bg,fg="#233D4D").grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Times New Roman',30, 'bold'),fg=frame_bg,bg="#233D4D",border=4,relief='raised').grid(row = 2, column = 2)

    Label(frame1, text="",bg="#A1C181").grid(row = 3,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 4,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.jpg")).resize((25,38)))
    congImg = Label(frame1, image=congLogo).grid(row = 5,column = 0)
    
    Label(frame1, text="    Cong:                       ", font=('Times New Roman',30, 'bold'),bg=frame_bg,fg="#233D4D").grid(row = 5, column = 1)
    Label(frame1, text=result['cong'], font=('Times New Roman',30, 'bold'),fg=frame_bg,bg="#233D4D",border=4,relief='raised').grid(row = 5, column = 2)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 6,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 7,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30)))
    aapImg = Label(frame1, image=aapLogo).grid(row = 8,column = 0)
    
    Label(frame1, text="    AAP:                         ", font=('Times New Roman',30, 'bold'),bg=frame_bg,fg="#233D4D").grid(row = 8, column = 1)
    Label(frame1, text=result['aap'], font=('Times New Roman',30, 'bold'),fg=frame_bg,bg="#233D4D",border=4,relief='raised').grid(row = 8, column = 2)
    
    Label(frame1, text="",bg="#A1C181").grid(row = 9,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 10,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35)))
    ssImg = Label(frame1, image=ssLogo).grid(row = 11,column = 0)
    
    Label(frame1, text="  Shiv Sena:              ", font=('Times New Roman',30, 'bold'),bg=frame_bg,fg="#233D4D").grid(row = 11, column = 1)
    Label(frame1, text=result['ss'], font=('Times New Roman',30, 'bold'),fg=frame_bg,bg="#233D4D",border=4,relief='raised').grid(row = 11, column = 2)

    Label(frame1, text="",bg="#A1C181").grid(row = 12,column = 0)
    Label(frame1, text="",bg="#A1C181").grid(row = 13,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.jpg")).resize((35,25)))
    notaImg = Label(frame1, image=notaLogo).grid(row = 14,column = 0)

    Label(frame1, text="    NOTA:                      ", font=('Times New Roman',30, 'bold'),bg=frame_bg,fg="#233D4D").grid(row = 14, column = 1)
    Label(frame1, text=result['nota'], font=('Times New Roman',30, 'bold'),fg=frame_bg,bg="#233D4D",border=4,relief='raised').grid(row = 14, column = 2)

    frame1.pack()
    root.mainloop()

'''
if _name_ == "_main_":
        root = Tk()
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.configure(bg="#A1C181")
        frame1 = Frame(root)
        showVotes(root,frame1)'''