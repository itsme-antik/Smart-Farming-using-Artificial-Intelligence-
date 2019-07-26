# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:27:11 2019

@author: Antik
"""

from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
ph = StringVar()
c=StringVar()
phos = StringVar()
potas = StringVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   Ph=ph.get()
   country=c.get()
   prog=var1.get()
   P = phos.get()
   K = potas.get()
   print (name1)
   print (email)
   print (Ph)
   print (country)
   print(P)
   print (K)
   
   
             
label_0 = Label(root, text="Farmer Gateway",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Adhaar card",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Phone Number",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=ph)
entry_3.place(x=240,y=230)


label_4 = Label(root, text="State",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['West Bengal','Punjab','Delhi','Tamil Nadu','Madhya Pradesh','Assam','Rajpura','Chandigarh','Patiala'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your state') 
droplist.place(x=240,y=280)

label_5 = Label(root, text = "Phosphorous", width = 20, font=("bold", 10))
label_5.place (x = 70, y=330)

entry_5 = Entry(root, textvar = phos)
entry_5.place(x = 240, y = 330)

label_6 = Label(root, text = "Potassium", width = 20, font=("bold", 10))
label_6.place (x = 70, y=380)

entry_6 = Entry(root, textvar = potas)
entry_6.place(x = 240, y = 380)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)

root.mainloop()