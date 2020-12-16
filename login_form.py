from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("login screen")
lb1= Label(window, text="Enter Login Details", font="times 15 bold")
lb1.place(x=160, y=10)

lb2 = Label(window, text="Username", font=" times 15 bold")
lb2.place(x=160, y=80)

e1 = Entry(window)
e1.place(x=160, y=110)

lb3 = Label(window, text="Password", font=" times 15 bold")
lb3.place(x=160, y=140)

passEntry = Entry(window, show="*")
passEntry.place(x=160, y=170)

btn = Button(window, text="Login", font="times 15 bold")
btn.place(x=160, y=200)

btn1 = Button(window, text="forgot password", font="times 10")
btn1.place(x=160, y=255)

window.mainloop()