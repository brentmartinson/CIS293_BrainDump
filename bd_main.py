from tkinter import*

master=Tk()
master.geometry("800x300")

def button1(click):
    label=Label(frame1, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button2(click):
    label=Label(frame2, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button3(click):
    label=Label(frame3, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button4(click):
    label=Label(frame4, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button5(click):
    label=Label(frame5, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button6(click):
    label=Label(frame6, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button7(click):
    label=Label(frame7, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

def button8(click):
    label=Label(frame8, text="Welcome", fg="cadet blue", height="9", width="22")
    label.pack(side=TOP)

frame1=Frame(master, width=200, height=150, background="cadet blue")
frame1.grid(row=0, column=0)
frame1.bind("<ButtonRelease>", button1)

frame2=Frame(master, width=200, height=150, background="light cyan")
frame2.grid(row=0, column=1)
frame2.bind("<ButtonRelease>", button2)

frame3=Frame(master, width=200, height=150, background="cadet blue")
frame3.grid(row=0, column=2)
frame3.bind("<ButtonRelease>", button3)

frame4=Frame(master, width=200, height=150, background="light cyan")
frame4.grid(row=0, column=3)
frame4.bind("<ButtonRelease>", button4)


frame5=Frame(master, width=200, height=150, background="light cyan")
frame5.grid(row=1, column=0)
frame5.bind("<ButtonRelease>", button5)

frame6=Frame(master, width=200, height=150, background="cadet blue")
frame6.grid(row=1, column=1)
frame6.bind("<ButtonRelease>", button6)

frame7=Frame(master, width=200, height=150, background="light cyan")
frame7.grid(row=1, column=2)
frame7.bind("<ButtonRelease>", button7)

frame8=Frame(master, width=200, height=150, background="cadet blue")
frame8.grid(row=1, column=3)
frame8.bind("<ButtonRelease>", button8)

master.mainloop()