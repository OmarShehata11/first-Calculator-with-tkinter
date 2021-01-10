from tkinter import *


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")


screen = Entry(root, width=77, borderwidth=5)
screen.grid(row=1, columnspan=4, padx=0, pady=9)


def addButton(num):

    if num == ".":
        temp_num = screen.get()
        print(temp_num)
        screen.delete(0, END)
        screen.insert(0, f"{temp_num}"+num)
        print(screen.get())
        return float(screen.get())
    else:
        temp_num = screen.get()
        screen.delete(0, END)
        screen.insert(0, str(temp_num) + str(num))


def num_add():
    global MATH
    global tempValue
    MATH = "add"
    tempValue = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, str(tempValue) + " + ")


def num_sub():
    global MATH
    global tempValue
    MATH = "sub"
    tempValue = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, str(tempValue) + " - ")


def num_multi():
    global MATH
    global tempValue
    MATH = "multi"
    tempValue = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, str(tempValue) + " x ")


def num_dev():
    global MATH
    global tempValue
    MATH = "dev"
    tempValue = float(screen.get())
    screen.delete(0, END)
    screen.insert(0, str(tempValue) + " / ")


def num_equal():
    global MATH
    global tempValue
    if MATH == "add":
       tempValue2 = screen.get()
       tempValue2 = tempValue2.split(" + ")
       screen.delete(0, END)
       screen.insert(0, float(tempValue) + float(tempValue2[-1]))

    elif MATH == "sub" :
        tempValue2 = screen.get()
        tempValue2 = tempValue2.split(" - ")
        screen.delete(0, END)
        screen.insert(0, float(tempValue) - float(tempValue2[-1]))

    elif MATH == "multi":
        tempValue2 = screen.get()
        tempValue2 = tempValue2.split(" x ")
        screen.delete(0, END)
        screen.insert(0, float(tempValue) * float(tempValue2[-1]))

    elif MATH == "dev":
        tempValue2 = screen.get()
        tempValue2 = tempValue2.split(" / ")
        screen.delete(0, END)
        screen.insert(0, float(tempValue) / float(tempValue2[-1]))
    global ANS
    ANS = float(screen.get())


def clear():
    screen.delete(0, END)


def Ans():
    global ANS
    if ANS:
        screen.delete(0, END)
        screen.insert(0, ANS)


button_clear = Button(root, text="Clear", padx=90, pady=10, bg="lightblue", borderwidth=3, command=clear)
button_ANS = Button(root, text="ANS", padx=90, pady=10, bg="lightblue", borderwidth=3, command=Ans)


button_equal = Button(root, text="=", padx=40, pady=20, bg="lightblue", highlightcolor="black", command=num_equal)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: addButton(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: addButton(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: addButton(3))

button4 = Button(root, text="4", padx=40, pady=20, command=lambda: addButton(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: addButton(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: addButton(6))

button7 = Button(root, text="7", padx=40, pady=20, command=lambda: addButton(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: addButton(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: addButton(9))

button0 = Button(root, text="0", padx=40, pady=20, command=lambda: addButton(0))

button_add = Button(root, text="+", padx=90, pady=20, bg="lightgreen", command=num_add)
button_sub = Button(root, text="-", padx=90, pady=20, bg="lightgreen", command=num_sub)
button_multi = Button(root, text="x", padx=90, pady=20, bg="lightgreen", command=num_multi)
button_dev = Button(root, text="/", padx=90, pady=20, bg="lightgreen", command=num_dev)

button_dot = Button(root, text=".", padx=42, pady=20, command=lambda: addButton("."))


button_clear.grid(row=0, column=0, columnspan=3)
button_ANS.grid(row=0, column=2, columnspan=6)


button_equal.grid(row=5, column=2)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=5, column=0)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_multi.grid(row=4, column=3)
button_dev.grid(row=5, column=3)

button_dot.grid(row=5, column=1)

root.mainloop()
