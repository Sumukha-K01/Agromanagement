from tkinter import Tk,Label
root = Tk()
hello=Label(master=root,text='Hello')
hello.pack()
def func():
    hello.config(text='Hello World')
    # comments added 
root.mainloop()
