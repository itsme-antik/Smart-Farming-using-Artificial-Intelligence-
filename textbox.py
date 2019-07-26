# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:38:31 2019

@author: Antik
"""

from tkinter import *
a = Tk()
a.title('Window')
a.geometry("500x500")
b= StringVar() #this will store value of textbox, now we have to print it so

def com():
    c=b.get() #this will get the value in b
    labl2 = Label(text=c, font=20 ).pack()#it will print value in C

labl1 = Label (text='Functionality to a Button',font = 30).pack()  #Label
button1 = Button(text = 'Press to print', command = com).pack()
#com is a class
#now we have to create a function for button so that we can do something

text = Entry(textvariable = b).pack()
#we want to print whenever in text box so lets create object to store that value

a.mainloop()