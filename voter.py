#voter
import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
import ssl

def establish_connection():
    host = "localhost"
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ssl_context.load_verify_locations(cafile='server.crt')  # Specify the server's certificate
        # print(3)
    # Wrap the socket with SSL/TLS
    client_socket = ssl_context.wrap_socket(client_socket, server_hostname='localhost')
    client_socket.connect((host, port))

    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Times New Roman', 20, 'bold')).grid(row = 3, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root, frame1):
    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    frame_bg = "#A1C181"  # light green

    frame1.config(bg=frame_bg)

    Label(frame1, text="\n\n                      Voter Login                     ", bg="#A1C181", fg="#233D4D", font=('Times New Roman', 30, 'bold')).pack()
    Label(frame1, text="", bg=frame_bg).pack()

    # Frame for Voter ID
    frame_voter_id = Frame(frame1, bg=frame_bg)
    frame_voter_id.pack()

    Label(frame_voter_id, text="Voter ID:  ", anchor="e", justify=LEFT, font=('Times New Roman', 30), bg=frame_bg, fg="#233D4D").pack(side=LEFT, padx=30)
    e1 = Entry(frame_voter_id, font=('Times New Roman', 30, 'bold'))
    e1.pack(side=LEFT)

    Label(frame1, text="", bg=frame_bg).pack()

    # Frame for Password
    frame_password = Frame(frame1, bg=frame_bg)
    frame_password.pack()

    Label(frame_password, text=" Password:", anchor="e", justify=LEFT, font=('Times New Roman', 30), bg=frame_bg, fg="#233D4D").pack(side=LEFT, padx=30)
    e3 = Entry(frame_password, show='*', font=('Times New Roman', 30, 'bold'))
    e3.pack(side=LEFT)

    Label(frame1, text="", bg=frame_bg).pack()

    # Button color
    button_bg = "#FCCA46"  # Gold
    button_fg = "#A4031F"  # Maroon

    sub = Button(frame1, text="Login", width=10, bg=button_bg, fg=button_fg, relief="raised", borderwidth=10, font=('Times New Roman', 25, 'bold'), command=lambda: log_server(root, frame1, client_socket, e1.get(), e3.get()))
    sub.pack()

    frame1.pack()
    root.mainloop()



'''
if _name_ == "_main_":
        root = Tk()
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.configure(bg="#A1C181")
        frame1 = Frame(root)
        voterLogin(root,frame1)
'''