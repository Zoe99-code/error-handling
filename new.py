from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Exception Handling")

amount_label = Label(root, text="Please enter amount in account")
amount_label.pack()
amount_entry = Entry(root)
amount_entry.pack()


def check():
    funds = amount_entry.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("Insufficient Funds. "
                                 "Please deposit more funds.")
        else:
            messagebox.showinfo("Congratulations! You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Error. Please insert a number.")


check_btn = Button(root, text="Check Qualification", command=check)
check_btn.pack()
root.mainloop()
