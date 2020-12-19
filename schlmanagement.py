from tkinter import *

window = Tk()

window.geometry("700x500")
window.title("welcome screen")

def create_account():
    root = Toplevel(window)
    root.title("create account")
    root.geometry("300x400")

    label = Label(root, text="Create Account", font="times 12 bold")
    label.place(x=70, y=15)

    label1 = Label(root, text="First Name", font="times 12 bold")
    label1.place(x=50, y=50)

    e1 = Entry(root)
    e1.place(x=50, y=70)

    label2 = Label(root, text="second Name", font="times 12 bold")
    label2.place(x=50, y=90)

    e2 = Entry(root)
    e2.place(x=50, y=115)

    label3 = Label(root, text="Username", font="times 12 bold")
    label3.place(x=50, y=140)

    e3 = Entry(root)
    e3.place(x=50, y=170)

    label4 = Label(root, text="Password", font="times 12 bold")
    label4.place(x=50, y=200)

    passEntry = Entry(root, show="*")
    passEntry.place(x=50, y=230)

    label5 = Label(root, text="Re-Enter Password", font="times 12 bold")
    label5.place(x=50, y=260)

    passEntry1 = Entry(root, show="*")
    passEntry1.place(x=50, y=290)

    label6 = Label(root, text="Subject", font="times 12 bold")
    label6.place(x=50, y=320)

    e4 = Entry(root)
    e4.place(x=50, y=350)

    btn = Button(root, text="Sign In", font="times 15 bold")
    btn.place(x=200, y=355)


def student_form():
    print("student account")

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

btn4 = Button(window, text="Create account",command=create_account, font="times 12 bold")
btn4.place(x=300, y=280)

window.mainloop()
