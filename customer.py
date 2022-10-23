import tkinter as tk
from tkinter import *
from collections import defaultdict
customers = {"Amazing": ("", "", "", "", "", "", "", 2.50), "targat": ("", "", "", "", "", "", "", 2.50)}
units = 10000
trans = defaultdict(int)
trans["Amazing"] = 10000
def add_customer():
    add = tk.Tk()
    add.title("Add Customer")
    add.geometry('450x350')

    # user information

    tk.Label(add, text='Company Name').place(x=20, y=10)
    company_name = tk.Entry(add)
    company_name.pack()
    company_name.place(x=20, y=30)
    tk.Label(add, text='Point of Contact').place(x=150, y=60)

    tk.Label(add, text='First Name').place(x=20, y=80)
    tk.Label(add, text='Last Name').place(x=250, y=80)
    first_name = tk.Entry(add)
    first_name.pack()
    first_name.place(x=20, y=100)
    last_name = tk.Entry(add)
    last_name.pack()
    last_name.place(x=250, y=100)

    tk.Label(add, text='Address 1').place(x=150, y=120)
    address1 = tk.Entry(add,width=50)
    address1.pack()
    address1.place(x=20, y=140)
    tk.Label(add, text='Address 2').place(x=150, y=160)
    address2 = tk.Entry(add, width=50)
    address2.pack()
    address2.place(x=20, y=180)

    tk.Label(add, text='City').place(x=100, y=200)
    city = tk.Entry(add, width=30)
    city.pack()
    city.place(x=20, y=220)

    tk.Label(add, text='State').place(x=20, y=240)
    tk.Label(add, text='Zip Code').place(x=250, y=240)
    state = tk.Entry(add)
    state.pack()
    state.place(x=20, y=260)
    zip_code = tk.Entry(add)
    zip_code.pack()
    zip_code.place(x=250, y=260)

    def submit():
        customers[company_name.get()] = (first_name.get(), last_name.get(), address1.get(), address2.get(),
                                         city.get(), state.get(), zip_code.get(), 2.50)
    submit = Button(add, text="submit", command=submit)
    submit.place(x=160, y=320)


def view_customer():
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=15, fg='blue',
                                   font=('Arial', 14, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    # take the data
    lst = [("Company Name", "Last Name", "First Name", "Address Line 1", "Address Line 2", "City", "State", "Zip Code", "Price($)")]
    for k, v in customers.items():
        lst.append((k, ) + v)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("All Customers")
    Table(view)


def create_invoice():
    global units
    add = tk.Tk()
    add.title("Create invoice")
    add.geometry('450x300')
    tk.Label(add, text='Select Customer').place(x=20, y=40)
    scrollbar = Scrollbar(add)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(add, yscrollcommand=scrollbar.set)
    for k in customers.keys():
        mylist.insert(END, k)

    mylist.pack(side=LEFT)
    scrollbar.config(command=mylist.yview)
    tk.Label(add, text='Number of Units in Stock').place(x=150, y=60)
    l = Label(add)
    l.configure(text=units)
    l.pack()
    l.place(x=170, y=80)
    tk.Label(add, text='Number of Units to invoice').place(x=150, y=100)
    num = tk.Entry(add)
    num.pack()
    num.place(x=150, y=120)

    def submit():
        global units
        c = mylist.selection_get()
        n = int(num.get())
        trans[c] += n
        units -= n
        l.configure(text=units)

    submit = Button(add, text="submit", command=submit)
    submit.place(x=160, y=270)
    add.mainloop()