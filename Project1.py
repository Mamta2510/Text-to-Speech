from tkinter import *
from gtts import gTTS
from playsound import playsound
def play():
    Message = entry_field.get()
    speech = gTTS(text= Message)
    speech.save("Tkinter.mp3")
    playsound("Tkinter.mp3")

def exit():
    root.destroy()

def reset():
    Msg.set("")

root = Tk()

root.title("TEXT TO SPEECH")
root.geometry("455x355")
root.configure(bg="ghost white")

Label(root, text="Text-to-Speech", font="lucida 25 bold").pack(fill=BOTH)
Label(root, text="Tkinter", relief=SUNKEN).pack(side=BOTTOM, fill=X)
Label(root, text="Enter Text", font="arial 15 bold", padx=5, pady=5).place(x=20, y=60)

Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, font="arial 10 bold", width="50")
entry_field.place(x=20, y=100)

Button(root, text="PLAY", font="lucida 20 bold",command=play).place(x=25, y=200)
Button(root, text="EXIT", font="lucida 20 bold", command=exit).place(x=150, y=200)
Button(root, text="RESET", font="lucida 20 bold", command=reset).place(x=275, y=200)
root.mainloop()