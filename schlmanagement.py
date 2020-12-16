from tkinter import *

window = Tk()

window.geometry("700x500")
window.title("welcome screen")

lb1 = Label(window, text="Welcome to Excel High School", font="times 20 bold")
lb1.place(x=180, y=10)

lb2 =Label(window, text="Motto :", font="times 15 bold")
lb2.place(x=180, y=80)

lb3 = Label(window, text="Education is the key", font="times 15 bold")
lb3.place(x=280, y=80)

lb4 = Label(window, text="Login As", font="times 15 bold")
lb4.place(x=280, y=140)

btn1 = Button(window, text="Student", font="times 15 bold")
btn1.place(x=200, y=200)

btn2 = Button(window, text="Teacher", font="times 15 bold")
btn2.place(x=320, y=200)

btn3 = Button(window, text="Worker", font="times 15 bold")
btn3.place(x=445, y=200)

window.mainloop()