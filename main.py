import tkinter
from tkinter import *
import time

root = Tk()
root.title("MyCalculator")

E = Entry(root, width=50, borderwidth=5, bg="cyan")
E.grid(row=0, column=0, columnspan=4)

"""Clicking to display clicked number"""
def button_click(number):
    current = E.get()
    E.delete(0, END)
    E.insert(0, str(current) + str(number))

"""Clear button"""
def button_clear():
    E.delete(0, END)

"""Addition"""
def button_add():
    first_number = E.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    E.delete(0, END)

"""Multiplication"""
def button_multiply():
    first_number = E.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    E.delete(0, END)

"""Substraction"""
def button_subs():
    first_number = E.get()
    global f_num
    global math
    math = "substract"
    f_num = int(first_number)
    E.delete(0, END)

"""Division"""
def button_divide():
    first_number = E.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    E.delete(0, END)

"""Smallest number"""
def min_num():
    first_number = E.get()
    global f_num
    global math
    math = "smallest"
    f_num = int(first_number)
    E.delete(0, END)

"""Biggest number"""
def max_num():
    first_number = E.get()
    global f_num
    global math
    math = "greater"
    f_num = int(first_number)
    E.delete(0, END)

"""Is Equal to sign"""
def button_equal():
    second_number = E.get()
    E.delete(0, END)

    """If and Else statement to decide what to equal to"""
    if math == "addition":
        E.insert(0, f_num + int(second_number))
    elif math == "multiply":
        E.insert(0, f_num * int(second_number))
    elif math == "substract":
        E.insert(0, f_num - int(second_number))
    elif math == "divide":
        E.insert(0, f_num / int(second_number))
    elif math == "smallest":
        E.insert(0, min(f_num, int(second_number)))
    elif math == "greater":
        E.insert(0, max(f_num, int(second_number)))


"""Creating the buttons and placing it on screen"""
b1 = Button(root, text="7", padx=30, pady=30, command=lambda: button_click(7)).grid(row=1, column=0)
b2 = Button(root, text="8", padx=30, pady=30, command=lambda: button_click(8)).grid(row=1, column=1)
b3 = Button(root, text="9", padx=30, pady=30, command=lambda: button_click(9)).grid(row=1, column=2)

b4 = Button(root, text="4", padx=30, pady=30, command=lambda: button_click(4)).grid(row=2, column=0)
b5 = Button(root, text="5", padx=30, pady=30, command=lambda: button_click(5)).grid(row=2, column=1)
b6 = Button(root, text="6", padx=30, pady=30, command=lambda: button_click(6)).grid(row=2, column=2)

b7 = Button(root, text="1", padx=30, pady=30, command=lambda: button_click(1)).grid(row=3, column=0)
b8 = Button(root, text="2", padx=30, pady=30, command=lambda: button_click(2)).grid(row=3, column=1)
b9 = Button(root, text="3", padx=30, pady=30, command=lambda: button_click(3)).grid(row=3, column=2)

b10 = Button(root, text="0", padx=30, pady=30, command=lambda: button_click(0)).grid(row=4, column=2)

b11 = Button(root, text="x", padx=30, pady=30, command=lambda: button_multiply()).grid(row=2, column=3)
b12 = Button(root, text="-", padx=30, pady=30, command=lambda: button_subs()).grid(row=3, column=3)
b13 = Button(root, text="+", padx=28, pady=30, command=lambda: button_add()).grid(row=4, column=3)
b14 = Button(root, text="/", padx=30, pady=30, command=lambda: button_divide()).grid(row=1, column=3)
b15 = Button(root, text="min", padx=24, pady=30, command=lambda: min_num()).grid(row=4, column=0)
b16 = Button(root, text="max", padx=24, pady=30, command=lambda: max_num()).grid(row=4, column=1)

b17 = Button(root, text="clear", padx=65, pady=30, command=lambda: button_clear()).grid(row=5, column=0, columnspan=2)
b18 = Button(root, text="=", padx=65, pady=30, command=lambda: button_equal()).grid(row=5, column=2, columnspan=2)

"""Main event loop"""
root.mainloop()














