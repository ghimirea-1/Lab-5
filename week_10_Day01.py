import tkinter as tk
#from tkinter.simpledialog import askinteger
from tkinter import *
#from tkinter import messagebox


top = Tk()



top.geometry("700x700")
answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)
        # elif x == "+/-":
        #     ans = eval(answer.get(1.0, "end-1c")).strip()
        #     if ans:
        #         if ans[0] == "-":
        #             answer.delete(0, 1)
        #         else:
        #             answer.insert(0, '-')
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)


B1 = Button(top, text="C", width=24, height=5, command=lambda: show("C"))
B1.place(x=100, y=150)
# B2 = Button(top, text="+/-", width=10, height=5, command=lambda: show("+/-"))
# B2.place(x=200, y=150)
B3 = Button(top, text="%", width=10, height=5, command=lambda: show("*100"))
B3.place(x=300, y=150)
B4 = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
B4.place(x=400, y=150)

B1 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B1.place(x=100, y=250)
B2 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B2.place(x=200, y=250)
B3 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B3.place(x=300, y=250)
B4 = Button(top, text="x", width=10, height=5, command=lambda: show("*"))
B4.place(x=400, y=250)

B1 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B1.place(x=100, y=350)
B2 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B2.place(x=200, y=350)
B3 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B3.place(x=300, y=350)
B4 = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
B4.place(x=400, y=350)


B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=450)
B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=450)
B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=300, y=450)
B4 = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
B4.place(x=400, y=450)

B1 = Button(top, text="0", width=24, height=5, command=lambda: show("0"))
B1.place(x=100, y=550)
B2 = Button(top, text=".", width=10, height=5, command=lambda: show("."))
B2.place(x=300, y=550)
B4 = Button(top, text="=", width=10, height=5, command=lambda: show("="))
B4.place(x=400, y=550)

top.mainloop()