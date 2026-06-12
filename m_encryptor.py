from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    print("")

def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="Encypt",font="arial",fg="black",bg="white").place(x=10,y=0)
        text2=Text(screen1,font="Roboto 10", bg="black",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)



def main_screen():

    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("500x398")
    
    #icon
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    screen.title("Encryptor")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for Encrypt or decrypt",fg="white",font=("calbri",13)).place(x=10,y=10)    
    text1=Text(font="Robote 20",bg="black",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption or decryption",fg="white",font=("calibri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=2,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="black",bd=1,command=encrypt).place(x=10,y=250)
    Button(text="Decrypt",height="2",width=23,bg="#00bd56",fg="black",bd=1,command=decrypt).place(x=240,y=250)
    Button(text="Reset",height="2",width=50,bg="#FFBF00",fg="black",bd=1,command=reset).place(x=10,y=300)

    

    screen.mainloop()

main_screen()
