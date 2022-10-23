import tkinter as tk
from tkinter import *
from collections import defaultdict

vendors = {"Tires R Us": ("Tire", 0.02, "", "", "", "", ""), "Mr. Mixers": ("Mixer", 0.05, "", "", "", "", "")}
p = defaultdict(float)
q = defaultdict(int)
p["Tire"] = 0.02
p["Mixer"] = 0.05
q["Tire"], q["Mixer"] = 10000, 10000


def add_vendor():
    add = tk.Tk()
    add.title("Add Vendor")
    add.geometry('450x350')

    # user information

    tk.Label(add, text='Vendor Name').place(x=20, y=10)
    vendor_name = tk.Entry(add)
    vendor_name.pack()
    vendor_name.place(x=20, y=30)
    tk.Label(add, text='Part Name').place(x=220, y=10)
    part_name = tk.Entry(add)
    part_name.pack()
    part_name.place(x=220, y=30)

    tk.Label(add, text='Price/Unit').place(x=20, y=60)
    price_name = tk.Entry(add)
    price_name.pack()
    price_name.place(x=20, y=80)

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
        vendors[vendor_name.get()] = (part_name.get(),  price_name.get(), address1.get(), address2.get(),
                                         city.get(), state.get(), zip_code.get())
    submit = Button(add, text="submit", command=submit)
    submit.place(x=160, y=300)


def view_vendor():
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
    lst = [("Vendor Name", "Part", "Price/Unit($)", "Address Line 1", "Address Line 2", "City", "State", "Zip Code")]
    for k, v in vendors.items():
        lst.append((k, ) + v)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("All Customers")
    Table(view)


def po():
    add = tk.Tk()
    add.title("Purchase order")
    add.geometry('450x300')

    tk.Label(add, text='Select Part').place(x=20, y=40)
    scrollbar = Scrollbar(add)
    scrollbar.pack(side=RIGHT, fill=Y)

    prices = defaultdict(float)
    mylist = Listbox(add, yscrollcommand=scrollbar.set)
    for k in vendors.keys():
        mylist.insert(END, vendors[k][0])
        prices[vendors[k][0]] = vendors[k][1]

    mylist.pack(side=LEFT)
    scrollbar.config(command=mylist.yview)
    tk.Label(add, text='Quantity').place(x=150, y=60)
    num = tk.Entry(add)
    num.pack()
    num.place(x=150, y=80)

    def submit():
        p[mylist.selection_get()] += int(num.get()) * prices[mylist.selection_get()]
        q[mylist.selection_get()] += int(num.get())
    submit = Button(add, text="submit", command=submit)
    submit.place(x=160, y=270)
    add.mainloop()

def view_inventory():
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    # take the data
    lst = [("Part", "Price/Unit($)", "Quantity", "Value($)")]
    for k, v in vendors.items():
        t = (v[0], v[1], q[v[0]], p[v[0]])
        lst.append(t)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("All Inventory")
    Table(view)