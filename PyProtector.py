from tkinter import *
__author__ = "Panboggo"
import webbrowser
import sys
import os
import time
f = Tk()
os.system("clear")
close = 0
def Login():
    global close
    username = case.get()
    password = case1.get()
    x = (val.get())
    lunghezza = len(username)
    lunghezza1 = len(password)
    if username == "QuaLaTuaPassword" and password == "QuaLaTuaPassword" and x == 1:
        testo2 = Label(f, text = "Login eseguito", font = "Times 10 bold")
        testo2.pack(side = TOP)
        time.sleep(3)
        f.destroy()
    else:
        testo3 = Label(f, text = "Login fallito! Riprova", font = "Times 10 bold")
        testo3.pack(side = TOP)
    if lunghezza < 2 and lunghezza1 < 3:
        testo5 = Label(f,text = "\nPassword corta", font = "Times 10 bold")
        testo5.pack(side = TOP)
def log():
    mytelegram = "http://t.me/panbogfo"
    webbrowser.open(mytelegram)
def control():
    x = (val.get())
    if x == 1:
        case.insert(0, "QuaLaTuaPassword")
        case1.insert(0, "QuaLaTuaPassword")
    elif x == 0:
        case.delete(0, END)
        case1.delete(0,END)
def logger(Evento):
    global close
    username = case.get()
    password = case1.get()
    x = (val.get())
    lunghezza = len(username)
    lunghezza1 = len(password)
    if username == "QuaLaTuaPassword" and password == "QuaLaTuaPassword" and x == 1:
        testo2 = Label(f, text = "Login eseguito", font = "Times 10 bold")
        testo2.pack(side = TOP)
        time.sleep(3)
        f.destroy()
    else:
        testo3 = Label(f, text = "Login fallito! Riprova", font = "Times 10 bold")
        testo3.pack(side = TOP)
    if lunghezza < 2 and lunghezza1 < 3:
        testo5 = Label(f,text = "\nPassword corta", font = "Times 10 bold")
        testo5.pack(side = TOP)
def onclosing():
    quit()

val = IntVar()
f.title("PyProtector")
f.geometry("300x300")
f.configure()
if close == 0:
    f.protocol("WM_DELETE_WINDOW", onclosing)     

testo = Label(f,text = "Username", font = "Times 10 bold")
testo.pack(side = TOP)

case = Entry(f)
case.pack(side = TOP)
case.bind("<Return>", logger)

testo = Label(f, text = "Password", font = "Times 10 bold")
testo.pack(side = TOP)

case1 = Entry(f, show = '*')
case1.pack(side = TOP)
case1.bind("<Return>", logger)

casella = Checkbutton(f, text="Ricordami", onvalue = 1, offvalue = 0, variable = val, command = control)
casella.pack(pady = 5)
casella.deselect() 

b = Button(f, text = "Login", command = Login)
b.pack(side = TOP)

b1 = Button(f, text = "Forget Password?", command = log)
b1.pack(side = RIGHT)

f.mainloop()