from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        
    def Field1():
        top.title("Field 1")
        top.geometry("500x500")
        button1 = Button(top, text = 'close')
        button1.pack()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        top = Toplevel()
        # creating a button instance
        Field_1 = Button(self, text="FIELD 1",fg = 'red', command = top.Field1 )
        Field_2 = Button(self, text="FIELD 2", fg = 'green')
        Field_3 = Button(self, text="FIELD 3")
        Field_4 = Button(self, text="FIELD 4", fg ='brown')
        
        # placing the button on my window
        Field_1.place(x=123, y=10)
        Field_2.place(x=180, y=10)
        Field_3.place(x =123, y = 40)
        Field_4.place(x =180, y = 40)
        
    
root = Tk()
label = Label (text='Which field information do you want to see',font = 30).pack()
#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  