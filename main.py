from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authentication")
root.geometry("500x500")
myframe = Frame(root)
myframe.place(x=0, y=0, width=500, height=500)

label_text = StringVar()
lab_1 = Label(myframe, text="PLease Enter User Login")
lab_1.pack()
label1 = Label(myframe, text="Username: ")
label1.pack()
e1 = Entry(myframe)
e1.pack()
label2 = Label(myframe, text="Password: ")
label2.pack()
e2 = Entry(myframe, show="*")
e2.pack()
label3 = Label(myframe, text="", textvariable=label_text)


def membership():
    username = ["Zaid", "Lihle", "Liyah", "Jade", "Thando"]
    passwords = ["1111", "2222", "3333", "4444", "5555"]
    found = False
    for x in range(len(username)):
        if e1.get() == username[x] and e2.get() == passwords[x]:
            found = True
    if found:
        messagebox.showinfo("Access Info", "Access Granted")
        root.destroy()
        import new
    else:
        messagebox.showerror("Access Granted", "Access Denied")


mybutton = Button(myframe, text="Login", command=membership)
mybutton.pack()

root.mainloop()