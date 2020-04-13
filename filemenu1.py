#!/usr/bin/env python3


import tkinter as tk
from tkinter import ttk

import os
import time
from pynput.keyboard import Key, Controller

window = tk.Tk()

keyboard = Controller()

window.title("FILE ZIP")
window.minsize(300,200)


def function1():
    time.sleep(2)
    
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    time.sleep(0.2)    
    keyboard.type('terminal')
    time.sleep(0.2) 
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    keyboard.type('cd Desktop')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    keyboard.type('zip -e'+' ' +name.get()+'.zip'+ ' '+name.get()+'.'+extension.get())
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.type(password.get())
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    keyboard.type(password.get())
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    with keyboard.pressed(Key.cmd):
        keyboard.press('w')
        keyboard.release('w')
    
       


label = ttk.Label(window, text = "Enter File Name ",font=('Helvetica 18 bold'))
label.grid(column = 0, row = 0)
label = ttk.Label(window, text = "(Make sure the file is on Desktop)")
label.grid(column = 0, row = 1)
name = tk.StringVar()
extension = tk.StringVar()
password = tk.StringVar()

label = ttk.Label(window, text = "File name")
label.grid(column = 0, row = 4)
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 6)


label = ttk.Label(window, text = "Extension without the (.) E.g - rtf, txt, jpg")
label.grid(column = 0, row = 8)
passEntered = ttk.Entry(window, width = 15, textvariable = extension)
passEntered.grid(column = 0, row = 10)

label = ttk.Label(window, text = "Password")
label.grid(column = 0, row = 12)
passEntered = ttk.Entry(window, width = 15, textvariable = password)
passEntered.grid(column = 0, row = 14)




button = ttk.Button(window, text = "Protect File", command = function1)
button.grid(column= 0, row = 16)



window.mainloop()
