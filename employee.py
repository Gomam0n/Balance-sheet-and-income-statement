import tkinter as tk
from tkinter import *
from collections import defaultdict

employees = {"James": 60000, "Curry": 60000}
payment = defaultdict(float)


def add_employee():
    add = tk.Tk()
    add.title("Add Employee")
    add.geometry('450x300')

    # user information

    tk.Label(add, text='name: ').place(x=50, y=150)

    tk.Label(add, text='salary: ').place(x=50, y=190)

    name = tk.StringVar()

    entry_name = tk.Entry(add, textvariable=name)
    entry_name.pack()
    entry_name.place(x=160, y=150)

    salary = tk.StringVar()

    entry_salary = tk.Entry(add, textvariable=salary)
    entry_salary.pack()
    entry_salary.place(x=160, y=190)

    def submit():
        employees[entry_name.get()] = entry_salary.get()
    submit = Button(add, text="submit", command=submit)
    submit.place(x=160, y=230)


def view_employee():
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
    lst = [("Name", "Salary")]
    for k, v in employees.items():
        t = (k, "$" + str(v))
        lst.append(t)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("All Employees")
    Table(view)


def pay_employee():
    add = tk.Tk()
    add.title("Pay Employee")
    add.geometry('450x300')

    scrollbar = Scrollbar(add)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(add, yscrollcommand=scrollbar.set)
    for k in employees.keys():
        mylist.insert(END, k)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

    def submit():
        payment[mylist.selection_get()] += employees[mylist.selection_get()] / 12.0
    submit = Button(add, text="Pay one employee", command=submit, width=15)
    submit.place(x=160, y=230)

    def submit_all():
        for k, v in employees.items():
            payment[k] += v / 12.0
    submit_all = Button(add, text="Pay all employees", command=submit_all, width=15)
    submit_all.place(x=160, y=200)

    def payroll():
        e = mylist.selection_get()
        l = int(payment[e] // (employees[e] // 12))

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
        lst = [("Name", "Salary", "Federal tax", "State Tax Withholding", "Social Security Tax",
                "Medicare Tax", "Amount Paid")]
        s = (employees[e] / 12)
        fed, state, social, medi = round(s / 5.2, 2), round(s / 20.1, 2 ), round(s / 19.5, 2), round(s / 75, 2)
        amount = s - fed - state - social - medi
        t = (e, s, fed, state, social, medi, amount)
        for _ in range(l):
            lst.append(t)
        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])

        # create root window
        view = Tk()
        view.title("Payroll")
        Table(view)
    payroll = Button(add, text="Payroll check", command=payroll, width=15)
    payroll.place(x=160, y=170)
