from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        '''weatherButton = Button(self, text="Weather", command =  self.weather)
        soilButton = Button(self, text="Soil", command = self.soil)
        waterButton = Button(self, text="Water", command = self.water)
        fertilizerButton = Button(self, text="Fertilizer", command = self.fertilizer)
        exitButton = Button(self, text="Quit", command = self.exitwin)

        # placing the button on my window
        weatherButton.place(x=0, y=0)
        soilButton.place(x=55, y=0)
        waterButton.place(x =85, y = 0)
        fertilizerButton.place(x =130, y = 0)
        exitButton.place(x=0, y= 60)'''
        
        
        menu = Menu(self.master)
        self.master.config(menu = menu)
        
        script = Menu(menu)
        script.add_command(label = "Weather", command = self.weather)
        script.add_command(label = "Soil", command = self.soil)
        script.add_command(label = "Water", command = self.water)
        script.add_command(label = "Fertilizer", command = self.fertilizer)
        menu.add_cascade (label = 'Run Script', menu = script)
        
        graph = Menu(menu)
        graph.add_command(label = "Weather", command = self.weather)
        graph.add_command(label = "Soil", command = self.soil)
        menu.add_cascade (label = 'Graph', menu = graph)
        
        '''edit = Menu(menu)
        edit.add_command(label = 'Soil', command = self.soil)
        menu.add_cascade (label= 'Edit', menu = edit)'''
        
        
    def exitwin(self):
        exit()
        
    def weather(self):
        c = "Sending message regarding weather data"
        labl2 = Label (text=c, font=5 ).pack()
    
    def soil(self):
        c = "Sending message regarding soil data"
        labl2 = Label(text=c, font=5 ).pack()
    
    def water(self):
        c = "Water pumps started"
        labl2 = Label(text=c, font=5 ).pack()
    
    def fertilizer(self):
        c = "Fertilizer pumps started"
        labl2 = Label(text=c, font=5 ).pack()
     
root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  