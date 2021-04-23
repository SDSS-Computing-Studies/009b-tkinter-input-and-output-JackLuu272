"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""


import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("294x300")

opword1 = StringVar()
opword1.set("")
opword2 = StringVar()
opword2.set("")
opword3 = StringVar()
opword3.set("")
opword4 = s=StringVar()
opword4.set("")
opword5 = StringVar()
opword5.set("")
opword6 = StringVar()
opword6.set("")
opword7 = StringVar()
opword7.set("")

def clickFunction():
    colour1 = insert1.get()
    colour1 = str(colour1)
    colour2 = insert2.get()
    colour2 = str(colour2)
    noun1 = insert3.get()
    noun1 = str(noun1)
    tobeverb1 = insert4.get()
    tobeverb1 = str(tobeverb1)
    adj1 = insert5.get()
    adj1 = str(adj1)
    tobeverb2 = insert6.get()
    tobeverb2 = str(tobeverb2)
    noun2 = insert7.get()
    noun2 = str(noun2)
    out1.insert(0,colour1)
    out2.insert(0,colour2)
    out3.insert(0,noun1)
    out4.insert(0,tobeverb1)
    out5.insert(0,adj1)
    out6.insert(0,tobeverb2)
    out7.insert(0,noun2)

ins = Label(win, text = "Enter a word for each box, \neach word should be the same type listed on the boxes.")
sente1 = Label(win, text = "Roses are ")
sente2 = Label(win, text = "Violets are ")
ending = Label(win, text = "And so")
insert1 = Entry(win, width = 10)
insert2 = Entry(win, width = 10)
insert3 = Entry(win, width = 10)
insert4 = Entry(win, width = 10)
insert5 = Entry(win, width = 10)
insert6 = Entry(win, width = 10)
insert7 = Entry(win, width = 10)
inslab1 = Label(win, text = "colour:")
inslab2 = Label(win, text = "colour:")
inslab3 = Label(win, text = "noun:")
inslab4 = Label(win, text = "tobe-:")
inslab5 = Label(win, text = "adj:")
inslab6 = Label(win, text = "tobe-:")
inslab7 = Label(win, text = "noun:")
pressin = Button(win, text = "Insert words", command = clickFunction)
out1 = Entry(win, width = 10, text = opword1)
out2 = Entry(win, width = 10, text = opword2)
out3 = Entry(win, width = 10, text = opword3)
out4 = Entry(win, width = 10, text = opword4)
out5 = Entry(win, width = 10, text = opword5)
out6 = Entry(win, width = 10, text = opword6)
out7 = Entry(win, width = 10, text = opword7)

ins.place(x=0, y=0)
insert1.place(x=0, y=60)
insert2.place(x=65, y=60)
insert3.place(x=130, y=60)
insert4.place(x=0, y=110)
insert5.place(x=65, y=110)
insert6.place(x=130, y=110)
insert7.place(x=195, y=110)
inslab1.place(x =0, y =35)
inslab2.place(x =65, y =35)
inslab3.place(x =130, y =35)
inslab4.place(x =0, y =85)
inslab5.place(x =65, y =85)
inslab6.place(x =130, y =85)
inslab7.place(x =195, y =85)
pressin.place(x=0,y=132)
sente1.place(x=0, y = 160)
sente2.place(x=0, y = 180)
ending.place(x=0, y =218)
out1.place(x = 65, y = 160)
out2.place(x = 65, y = 180)
out3.place(x = 0, y = 200)
out4.place(x = 65, y = 200)
out5.place(x = 130, y = 200)
out6.place(x = 65, y = 218)
out7.place(x = 130, y = 218)

win.mainloop()