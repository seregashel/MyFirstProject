from tkinter import *
from tkinter import Label
from tkinter import messagebox
import random


def UnswerButton():
    if Unswer.get() == number:
        messagebox.showinfo("вы угадали", Unswer_text_win,)
    else:
        messagebox.showinfo("вы не угадали", Unswer_text_lose)

def Clear():
    Unswer_entry.delete(0,END)


root = Tk()
root.title("Угадай число")
root.geometry("300x250")

number = random.randint(1,10)

Text1 = Label(text="угадай число от 1 до 10")
Text1.pack()

Unswer = IntVar()


Unswer_text_win = "вы угадали"
Unswer_text_lose = "вы не угадали"

Unswer_entry = Entry(textvariable=Unswer)
Unswer_entry.place(relx=.3, rely=.1)

#кнопка ввести
btn = Button(text="ввести", command=UnswerButton)
btn.place(rely=.2, relx=.3)

#кнопка очтисть
btn_clear = Button(text="очистить",command=Clear)
btn_clear.place(rely=.2, relx=.5)
root.mainloop()