"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import *
import math

win = tk.Tk()
win.geometry("593x80")

xoutput1 = StringVar()
xoutput1.set("")
xoutput2 = StringVar()
xoutput2.set("")

def clickFunction():
    numberb = b.get()
    numberb = float(numberb)
    numberc = c.get()
    numberc = float(numberc)
    ans1 = 1 + math.sqrt(numberb**2 - 4*numberc)/2.0
    ans2 = 1 - math.sqrt(numberb**2 - 4*numberc)/2.0
    outputer1.insert(0,ans1)
    outputer2.insert(0,ans2)
    if numberb**2 - 4*numberc < 0:
        outputer1.insert(0,"invalid input")
        outputer2.insert(0,"try again")

instruct = Label(win, text = "Insert a value for b and c, click \"calculate\" to perfrom the calculation: ")
enter = Button(win, text = "calculate", command = clickFunction)
a = Label(win, text = "a")
x1 = Label(win, text = "x^2")
plus1 = Label(win, text = "+")
x2 = Label(win, text = "x")
plus2 = Label(win, text = "+")
equal = Label(win, text = "=")
zero = Label(win, text = "0")
b = Entry(win, width = 10)
c = Entry(win, width = 10)
outputer1 = Entry(win, width = 20, text = xoutput1)
outputer2 = Entry(win, width = 20, text = xoutput2)

instruct.grid(row = 1, column = 1, columnspan = 2)
a.grid(row = 1, column = 2)
x1.grid(row = 1, column = 3)
plus1.grid(row = 1, column = 4)
b.grid(row = 1, column = 5)
x2.grid(row = 1, column = 6)
plus2.grid(row = 1, column = 7)
c.grid(row = 1, column = 8)
equal.grid(row = 1, column = 9)
zero.grid(row = 1, column = 10)
enter.place(x=0,y=25)
outputer1.place(x=0, y=55)
outputer2.place(x=120, y=55)

win.mainloop()