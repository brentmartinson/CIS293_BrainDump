from tkinter import *
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="To Do:")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        print(self.value)

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.master.title("Brain Dump")
        self.button1=Button(master, width=20, height=10, command=self.popup)
        self.button1.grid(row=0, column=0)
        self.button2=Button(master, width=20, height=10, command=self.popup)
        self.button2.grid(row=0, column=1)
        self.button3=Button(master, width=20, height=10, command=self.popup)
        self.button3.grid(row=0, column=2)
        
        self.button4=Button(master, width=20, height=10, command=self.popup)
        self.button4.grid(row=1, column=0)
        self.button5=Button(master, width=20, height=10, command=self.popup)
        self.button5.grid(row=1, column=1)
        self.button6=Button(master, width=20, height=10, command=self.popup)
        self.button6.grid(row=1, column=2)

        self.button7=Button(master, width=20, height=10, command=self.popup)
        self.button7.grid(row=2, column=0)
        self.button8=Button(master, width=20, height=10, command=self.popup)
        self.button8.grid(row=2, column=1)
        self.button9=Button(master, width=20, height=10, command=self.popup)
        self.button9.grid(row=2, column=2)
        
    def popup(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def entryValue(self):
        return self.w.value

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
