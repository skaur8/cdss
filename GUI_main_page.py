#!/usr/bin/python3

from Tkinter import *
from ttk import * 

import Tkinter as tk
import sys
from Tkinter import *

#print 
assert sys.version_info >= (3)

LARGE_FONT= ("Verdana",12)

class Application(tk.Tk):

        def __init__(self,*args,**kwargs):
            tk.Tk.__init__(self,*args,**kwargs)
            tk.Tk.wm_title(self,"Optical Disorder Detector")
            container = tk.Frame(self)

            container.pack(side="top",fill="both",expand = True)

            container.grid_rowconfigure(0,weight=1)
            container.grid_columnconfigure(0,weight=1)

            self.frames = {}

            for F in (StartPage,PageOne,PageTwo):
            
             	frame = F(container,self)

            	self.frames[F] = frame

            	frame.grid(row=0,column=0,sticky="nsew")
                #frame.grid(row=110,column=110,sticky="nsew")

            self.show_frame(StartPage)

        def show_frame(self,cont):

               frame = self.frames[cont]
               frame.tkraise()

def qf():
    print("you did it!")

class StartPage(tk.Frame):

   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       #create frames
       f1 = Frame(self,width = 1600,height = 500,relief=SUNKEN)
       f1.pack()

       f2 = Frame(self,width = 1600,height = 700,relief=SUNKEN)
       f2.pack()

       #f3 = Frame(self,width = 500,height = 700,relief=SUNKEN)
       #f3.pack(side=RIGHT)
       #create labels
       label2 = tk.Label(f1,text="Optical Disorder Detector",font=LARGE_FONT)	
       label2.pack()
	
       label = tk.Label(f1,text="Home",font=LARGE_FONT)
       label.pack()
       label1 = tk.Label(f1,text="Sign Out",font=LARGE_FONT)
       label1.pack()  
       
       
       label3 = tk.Label(f1,text="Age",font=('arial',10,'bold')) 
       label3.pack() 
       
       #create combobox for age 
       v = [1,2,3,4,5,6,7,8,9,10]

       combo = Combobox(f1,values=v,height=2)
       combo.pack()

       label4 = tk.Label(f1,text="Gender")
       label4.pack()
       
       #create radio buttons
       r1 = Radiobutton(f1,text="male",value=1)
       r2 = Radiobutton(f1,text="female",value=2) 
       r1.pack()
       r2.pack() 

       label5 = tk.Label(f2,text="Symptoms")
       label5.pack()
       
       #create combobox for symptoms  	
       v = ["Diabetes","Blood Pressure"]

       combo = Combobox(f2,values=v,height=2)
       combo.pack()
       
       print(combo.get())
       button1 = tk.Button(self,text="Predict",command=lambda:controller.show_frame(PageOne))
       button1.pack()
       


       label6 = tk.Label(f2,text="Current Medical Conditions")
       label6.pack()           

       v = ["Diabetes","Blood Pressure"]

       combo = Combobox(f2,values=v,height=2)
       combo.pack()

       #button1 = tk.Button(self,text="Predict",command=lambda:controller.show_frame(PageOne))
       #button1.pack()

       button2 = tk.Button(self,text="Page Two",command=lambda:controller.show_frame(PageTwo))
       button2.pack()

class PageOne(tk.Frame):
   
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       #label = tk.Label(self,text="Start Page",font=LARGE_FONT)
       #label.pack(pady=10,padx=10)

       button1 = tk.Button(self,text="Home",command=lambda:controller.show_frame(StartPage))
       button1.pack()

       button2 = tk.Button(self,text="Page Two",command=lambda:controller.show_frame(PageTwo))
       button1.pack()

       f2 = Frame(self,width = 800,height = 700,relief=SUNKEN)
       f2.pack(side=LEFT)

       label1 = tk.Label(f2,text="About Disorder",font=('arial',10,'bold')) 
       label1.pack() 

       label2 = tk.Label(f2,text="Relief Measures",font=('arial',10,'bold')) 
       label2.pack()  	
       
       label2 = tk.Label(f2,text="Exercise",font=('arial',10,'bold')) 
       label2.pack()  	

       label2 = tk.Label(f2,text="Diet",font=('arial',10,'bold')) 
       label2.pack()  	
    
       

class PageTwo(tk.Frame):
   
   def __init__(self,parent,controller):
       tk.Frame.__init__(self,parent)
       #label = tk.Label(self,text="Home",font=LARGE_FONT)
       #label.pack(pady=10,padx=10)

       button1 = tk.Button(self,text="Home",command=lambda:controller.show_frame(StartPage))
       button1.pack()

app = Application()
app.mainloop()

