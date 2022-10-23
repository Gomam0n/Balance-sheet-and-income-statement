import tkinter as tk
from tkinter import *
from employee import *
from customer import *
from vendor import *

menu = tk.Tk()
menu.title("TE566 Computer Porgram")
menu.geometry('600x400')

def show_balance():
    print(payment)
    num_of_pro = 0
    for k, v in trans.items():
        num_of_pro += v
    sales = num_of_pro * 2.5
    cogs = 0
    for k, v in q.items():
        cogs += v * p[k]
    gross_profit = sales - cogs
    payroll = 0
    for k, v in payment.items():
        payroll += v
    payroll_with = payroll / 3
    bill = 1000
    annual_expense = 10000

    total_exp = payroll + payroll_with + bill + annual_expense
    other_income = 0
    income_taxes = (gross_profit + other_income - total_exp) * 0.2

    net_income = gross_profit + other_income - total_exp - income_taxes

    cash = 100000 + net_income
    receiveable = 0
    inventory = cogs
    total_curr_assets = cash + receiveable + inventory
    buildings, equipments, furnitures = 0, 10000, 0
    total_fixed_assets = buildings + equipments + furnitures
    total_assets = total_curr_assets + total_fixed_assets

    payable = 0
    total_current_debt = payable

    mortage = buildings + equipments + furnitures
    total_long_term_debt = mortage

    total_liabiliaties = total_long_term_debt + total_curr_assets

    net_worth = total_assets - total_liabiliaties
    total_li_and_net_worth = total_assets
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=25, fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    lst = [["Cash", "$" + str(cash), "", "Account Payable", "$" + str(payable)],
           ["Account Receivable", "$"+str(receiveable), "", "",""],
           ["Inventory", "$" + str(inventory), "", "", ""],
           ["Total Current Assets", "$" + str(total_curr_assets), "", "Total Current Liabilities", "$"+str(total_current_debt)],
           ["", "", "","",""],
           ["Buildings", "$" +str(buildings), "", "Mortgage", "$"+str(mortage)],
           ["Equipment", "$" + str(equipments), "", "Total Long Term Debt", "$" + str(total_long_term_debt)],
           ["Furniture", "$" +str(furnitures), "", "", ""],
           ["Total Fixed Assets", "$" + str(total_fixed_assets), "", "Total Liabilities", "$"+str(total_liabiliaties)],
           ["", "", "", "Net Worth", "$" + str(net_worth)],
           ["Total Assets", "$" +str(total_assets), "", "Total Liablities & Net Worth", "$" +str(total_li_and_net_worth)],
           ]
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("Balance sheet")
    Table(view)
def show_income():
    num_of_pro = 0
    for k, v in trans.items():
        num_of_pro += v
    sales = num_of_pro * 2.5
    cogs = 0
    for k, v in q.items():
        cogs += v * p[k]
    gross_profit = sales - cogs
    payroll = 0
    for k, v in payment.items():
        payroll += v
    payroll_with = payroll / 3
    bill = 1000
    annual_expense = 10000

    total_exp = payroll + payroll_with + bill + annual_expense
    other_income = 0
    income_taxes = (gross_profit + other_income - total_exp) * 0.2

    net_income = gross_profit + other_income - total_exp - income_taxes
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    lst = [["Sales", "$" + str(sales)], ["COGS", "$" + str(cogs)], ["Gross Profit", "$" + str(gross_profit)],
           ["", ""], ["Expenses", ""], ["Payroll", "$" + str(payroll)],
            ["Payroll Withholding", "$" + str(payroll_with)], ["Bills", "$" + str(bill)],
            ["Annual Expenses", "$" + str(annual_expense)], ["Total Expenses", "$" + str(total_exp)],
            ["",""], ["Other Income", "$"+str(other_income)], ["Income Taxes", "$" +str(income_taxes)],
           ["Net income", "$" + str(net_income)]
                                        ]
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    view = Tk()
    view.title("Income Statement")
    Table(view)


addEmployee = Button(menu, text="Add Employee", command=add_employee, width=25)
addEmployee.grid(row=1, column=2)

viewEmployee = Button(menu, text="View Employee", command=view_employee, width=25)
viewEmployee.grid(row=1, column=3)

payEmployee = Button(menu, text="Pay Employee", command=pay_employee, width=25)
payEmployee.grid(row=1, column=4)

addCustomer = Button(menu, text="Add Customer", command=add_customer, width=25)
addCustomer.grid(row=2, column=2)

viewCustomer = Button(menu, text="View Customer", command=view_customer, width=25)
viewCustomer.grid(row=2, column=3)

invoice = Button(menu, text="Create Invoice", command=create_invoice, width=25)
invoice.grid(row=2, column=4)

addVendor = Button(menu, text="Add Vendor", command=add_vendor, width=25)
addVendor.grid(row=3, column=2)

viewVendor = Button(menu, text="View Vendor", command=view_vendor, width=25)
viewVendor.grid(row=3, column=3)

po = Button(menu, text="Purchase Order", command=po, width=25)
po.grid(row=3, column=4)

inventory = Button(menu, text="View Inventory", command=view_inventory, width=25)
inventory.grid(row=4, column=3)

balance = Button(menu, text="Show Balance Sheet", command=show_balance, width=25)
balance.grid(row=5, column=3)

income = Button(menu, text="Show Income Statement", command=show_income, width=25)
income.grid(row=6, column=3)
menu.mainloop()
