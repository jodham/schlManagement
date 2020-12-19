from tkinter import *

window = Tk()

window.geometry("700x500")
window.title("welcome screen")
#register user account------------------------start
def signup_user():
    firstName_info = firstName.get()
    secondName_info = secondName.get()
    username_info = username.get()
    password_info = password.get()
    subject_info = subject.get()

#register user account-------------------------end
#create account form___________________________start
def create_account():
    root = Toplevel(window)
    root.title("create account")
    root.geometry("300x400")

    global firstName
    global secondName
    global username
    global password
    global subject

    label = Label(root, text="Create Account", font="times 12 bold")
    label.place(x=70, y=15)

    label1 = Label(root, text="First Name", font="times 12 bold")
    label1.place(x=50, y=50)

    e1 = Entry(root, textvariable = firstName)
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

    btn = Button(root, text="Sign Up",command = signup_user, font="times 15 bold")
    btn.place(x=200, y=355)
#create account form--------------------------------end


#student login form---------------------start


def student_login():
    stud_login = Toplevel(window)
    stud_login.geometry("500x500")
    stud_login.title("login screen")
    lb1 = Label(stud_login, text="Student Account", font="times 15 bold",fg="orange")
    lb1.place(x=160, y=5)
    lb1 = Label(stud_login, text="Enter Login Details", font="times 13 bold")
    lb1.place(x=160, y=40)

    lb2 = Label(stud_login, text="Username", font=" times 15 bold")
    lb2.place(x=160, y=80)

    e1 = Entry(stud_login)
    e1.place(x=160, y=110)

    lb3 = Label(stud_login, text="Password", font=" times 15 bold")
    lb3.place(x=160, y=140)

    passEntry = Entry(stud_login, show="*")
    passEntry.place(x=160, y=170)

    btn = Button(stud_login, text="Login", font="times 15 bold")
    btn.place(x=160, y=200)

    btn1 = Button(stud_login, text="forgot password", font="times 10")
    btn1.place(x=160, y=255)
#student login form ---------------------------------end


#teacher login form ----------------------------------start
def teach_login():
    teacher_login = Toplevel()
    teacher_login.geometry("500x500")
    teacher_login.title("login screen")
    lb1 = Label(teacher_login, text="Teacher Account", font="times 15 bold",fg="orange")
    lb1.place(x=160, y=5)
    lb1 = Label(teacher_login, text="Enter Login Details", font="times 13 bold")
    lb1.place(x=160, y=40)

    lb2 = Label(teacher_login, text="Username", font=" times 15 bold")
    lb2.place(x=160, y=80)

    e1 = Entry(teacher_login)
    e1.place(x=160, y=110)

    lb3 = Label(teacher_login, text="Password", font=" times 15 bold")
    lb3.place(x=160, y=140)

    passEntry = Entry(teacher_login, show="*")
    passEntry.place(x=160, y=170)

    btn = Button(teacher_login, text="Login", font="times 15 bold")
    btn.place(x=160, y=200)

    btn1 = Button(teacher_login, text="forgot password", font="times 10")
    btn1.place(x=160, y=255)


#teacher login form ------------------------------------end

#worker login form --------------------------------------start
def worker_account():
    worker_login = Toplevel()
    worker_login.geometry("500x500")
    worker_login.title("login screen")
    lb1 = Label(worker_login, text="Worker Account", font="times 15 bold",fg="orange")
    lb1.place(x=160, y=5)
    lb1 = Label(worker_login, text="Enter Login Details", font="times 13 bold")
    lb1.place(x=160, y=40)

    lb2 = Label(worker_login, text="Username", font=" times 15 bold")
    lb2.place(x=160, y=80)

    e1 = Entry(worker_login)
    e1.place(x=160, y=110)

    lb3 = Label(worker_login, text="Password", font=" times 15 bold")
    lb3.place(x=160, y=140)

    passEntry = Entry(worker_login, show="*")
    passEntry.place(x=160, y=170)

    btn = Button(worker_login, text="Login", font="times 15 bold")
    btn.place(x=160, y=200)

    btn1 = Button(worker_login, text="forgot password", font="times 10")
    btn1.place(x=160, y=255)


#worker login form ------------------------------------------end
lb1 = Label(window, text="Welcome to Excel High School", font="times 20 bold")
lb1.place(x=180, y=10)

lb2 =Label(window, text="Motto :", font="times 15 bold")
lb2.place(x=180, y=80)

lb3 = Label(window, text="Education is the key", font="times 15 bold")
lb3.place(x=280, y=80)

lb4 = Label(window, text="Login As", font="times 15 bold")
lb4.place(x=280, y=140)

btn1 = Button(window, text="Student",command=student_login, font="times 15 bold")
btn1.place(x=200, y=200)

btn2 = Button(window, text="Teacher",command = teach_login, font="times 15 bold")
btn2.place(x=320, y=200)

btn3 = Button(window, text="Worker",command = worker_account, font="times 15 bold")
btn3.place(x=445, y=200)

btn4 = Button(window, text="Create account",command=create_account, font="times 12 bold")
btn4.place(x=300, y=280)

window.mainloop()
