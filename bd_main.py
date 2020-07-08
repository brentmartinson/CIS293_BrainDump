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
        
        self.button1_text = StringVar()
        self.button1_text.set("this is a test of what it would look like to have a todo item in this cell")
        self.button1=Button(master, width=20, height=10, wraplength=170, textvariable=self.button1_text, command=self.addToDo1)
        self.button1.grid(row=0, column=0)
        self.button2_text = StringVar()
        self.button2_text.set("")
        self.button2=Button(master, width=20, height=10, wraplength=170, textvariable=self.button2_text, command=self.addToDo2)
        self.button2.grid(row=0, column=1)
        self.button3_text = StringVar()
        self.button3_text.set("")
        self.button3=Button(master, width=20, height=10, wraplength=170, textvariable=self.button3_text, command=self.addToDo3)
        self.button3.grid(row=0, column=2)
        
        self.button4_text = StringVar()
        self.button4_text.set("")
        self.button4=Button(master, width=20, height=10, wraplength=170, textvariable=self.button4_text, command=self.addToDo4)
        self.button4.grid(row=1, column=0)
        self.button5_text = StringVar()
        self.button5_text.set("")
        self.button5=Button(master, width=20, height=10, wraplength=170, textvariable=self.button5_text, command=self.addToDo5)
        self.button5.grid(row=1, column=1)
        self.button6_text = StringVar()
        self.button6_text.set("")
        self.button6=Button(master, width=20, height=10, wraplength=170, textvariable=self.button6_text, command=self.addToDo6)
        self.button6.grid(row=1, column=2)

        self.button7_text = StringVar()
        self.button7_text.set("")
        self.button7=Button(master, width=20, height=10, wraplength=170, textvariable=self.button7_text, command=self.addToDo7)
        self.button7.grid(row=2, column=0)
        self.button8_text = StringVar()
        self.button8_text.set("")
        self.button8=Button(master, width=20, height=10, wraplength=170, textvariable=self.button8_text, command=self.addToDo8)
        self.button8.grid(row=2, column=1)
        self.button9_text = StringVar()
        self.button9_text.set("")
        self.button9=Button(master, width=20, height=10, wraplength=170, textvariable=self.button9_text, command=self.addToDo6)
        self.button9.grid(row=2, column=2)
        
    def popup(self):
        self.w=popupWindow(self.master)
        self.master.wait_window(self.w.top)

    def addToDo1(self):
        self.popup()
        self.button1_text.set(self.w.value)

    def addToDo2(self):
        self.popup()
        self.button2_text.set(self.w.value)
    
    def addToDo3(self):
        self.popup()
        self.button3_text.set(self.w.value)
    
    def addToDo4(self):
        self.popup()
        self.button4_text.set(self.w.value)
    
    def addToDo5(self):
        self.popup()
        self.button5_text.set(self.w.value)
    
    def addToDo6(self):
        self.popup()
        self.button6_text.set(self.w.value)

    def addToDo7(self):
        self.popup()
        self.button7_text.set(self.w.value)

    def addToDo8(self):
        self.popup()
        self.button8_text.set(self.w.value)
    
    def addToDo9(self):
        self.popup()
        self.button9_text.set(self.w.value)

if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()
