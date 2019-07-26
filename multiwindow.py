# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:42:51 2019

@author: Antik
"""

from tkinter import *


#field 1
def field1():
    top = Toplevel()
    top.title("Field 1")
    top.geometry("500x500")
    weather1 = Button(top, text = 'Weather conditions', command=weather_1).pack()
    soil1 = Button(top, text ="Soil Conditions", command=soil_1).pack()
    water1 =Button(top, text = "Start waterpumps", command =water_1).pack()
    fer1 = Button(top,text="Start fertilizers", command =fertilizer_1).pack()
def weather_1():
    c = "Weather data of field 1"
    labl2 = Label (text=c, font=5 ).pack()
def soil_1():
    c = "Soil data of field 1"
    labl2 = Label(text=c, font=5 ).pack()
def water_1():
    c = "Water pumps started in field 1"
    labl2 = Label(text=c, font=5 ).pack()
def fertilizer_1():
    c = "Fertilizer pumps started in field 1"
    labl2 = Label(text=c, font=5 ).pack()
    

    
#field 2
def field2():
    top = Toplevel()
    top.title("Field 2")
    top.geometry("500x500")
    weather2 = Button(top, text = 'Weather conditions', command=weather_2).pack()
    soil2 = Button(top, text ="Soil Conditions", command=soil_2).pack()
    water2 =Button(top, text = "Start waterpumps", command =water_2).pack()
    fer2 = Button(top,text="Start fertilizers", command =fertilizer_2).pack()
def weather_2():
    c = "Weather data of field 2"
    labl2 = Label (text=c, font=5 ).pack()
def soil_2():
    c = "Soil data of field 2"
    labl2 = Label(text=c, font=5 ).pack()
def water_2():
    c = "Water pumps started in field 2"
    labl2 = Label(text=c, font=5 ).pack()
def fertilizer_2():
    c = "Fertilizer pumps started in field 2"
    labl2 = Label(text=c, font=5 ).pack()
    
#field 3
def field3():
    top = Toplevel()
    top.title("Field 3")
    top.geometry("500x500")
    weather2 = Button(top, text = 'Weather conditions', command=weather_3).pack()
    soil2 = Button(top, text ="Soil Conditions", command=soil_3).pack()
    water2 =Button(top, text = "Start waterpumps", command =water_3).pack()
    fer2 = Button(top,text="Start fertilizers", command =fertilizer_3).pack()
def weather_3():
    c = "Weather data of field 3"
    labl2 = Label (text=c, font=5 ).pack()
def soil_3():
    c = "Soil data of field 3"
    labl2 = Label(text=c, font=5 ).pack()
def water_3():
    c = "Water pumps started in field 3"
    labl2 = Label(text=c, font=5 ).pack()
def fertilizer_3():
    c = "Fertilizer pumps started in field 3"
    labl2 = Label(text=c, font=5 ).pack()
    
    
#field 4
def field4():
    top = Toplevel()
    top.title("Field 4")
    top.geometry("500x500")
    weather2 = Button(top, text = 'Weather conditions', command=weather_4).pack()
    soil2 = Button(top, text ="Soil Conditions", command=soil_4).pack()
    water2 =Button(top, text = "Start waterpumps", command =water_4).pack()
    fer2 = Button(top,text="Start fertilizers", command =fertilizer_4).pack()
def weather_4():
    c = "Weather data of field 4"
    labl2 = Label (text=c, font=5 ).pack()
def soil_4():
    c = "Soil data of field 4"
    labl2 = Label(text=c, font=5 ).pack()
def water_4():
    c = "Water pumps started in field 4"
    labl2 = Label(text=c, font=5 ).pack()
def fertilizer_4():
    c = "Fertilizer pumps started in field 4"
    labl2 = Label(text=c, font=5 ).pack()
root = Tk()
label = Label (text='Which field information do you want to see',font = 30).pack()
button = Button (root, text = 'Field 1', command = field1, fg ='red').pack()
button = Button (root, text = 'Field 2', command = field2, fg ='green').pack()
button = Button (root, text = 'Field 3', command = field3).pack()
button = Button (root, text = 'Field 4', command = field4, fg = 'brown').pack()

root.geometry("500x500")
root.mainloop()

