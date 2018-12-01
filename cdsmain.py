from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import NaiveB as nb
import csv
import pandas as pd


LARGE_FONT= ("Verdana",16)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top",fill="both",expand= True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(1,weight=1)

        self.frames = {}

        for F in (PageOne, PageTwo, PageThree):
            
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)
        
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
    
    
class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.configure(background = 'LightBlue')
        
        label=tk.Label(self,text="OPTICAL DISORDER DETECTOR",font=LARGE_FONT)
        label.pack(pady=8,padx=8)

        var = IntVar()
        
        namelabel=tk.Label(self,text="Enter Patient name")
        name=input(Text(self,fg="Blue",height=1,width=40))
        namelabel.pack(pady=8,padx=8)
        name.pack()
        
        agelabel=Label(self,text="Enter Patient age")
        age=int(input(Text(self,fg="Blue",height=1,width=10)))
        agelabel.pack(pady=8,padx=8)
        age.pack()
        
        GenderLabel=Label(self, text="Select your gender")
        GenderLabel.pack(pady=8,padx=8)
        def sel():
           selection = "You selected the option " + str(var.get())
           l1=tk.Label(self,text = selection)
        selectmale= tk.Radiobutton(self, text="Male", variable=var, value=1,command=sel)
        selectfemale=tk.Radiobutton(self, text="Female", variable=var, value=2,command=sel)
        selectmale.pack(pady=5,padx=5)
        selectfemale.pack(pady=5,padx=5)
        
        symplab=tk.Label(self,text="Select your symptoms")
        symplab.pack(pady=8,padx=8)
        f1 = tk.Frame(self,width = 1600,height = 500,relief=SUNKEN)
        f1.pack()
        symps=StringVar()
        df1 = pd.read_csv("Optical Disorder - Sheet1.csv")
        symps = symps.set(df1.Symptoms)
        symbox = tk.Listbox(f1, listvariable=symps, selectmode=MULTIPLE, width=40, height=8)
        symbox.grid(column=0, row=0, columnspan=2)
        def select():
            reslist = list()
            selection = symbox.curselection()
            for i in selection:
                enter = symbox.get(i)
                reslist.append(enter)
            for val in reslist:
                val.append(reslist)
                

        medlab=tk.Label(self,text="Select your medical history if any")
        medlab.pack(pady=8,padx=8)
        
        f2 = tk.Frame(self,width = 1600,height = 500,relief=SUNKEN)
        f2.pack()
        
        

        medhis = StringVar()
        df2 = pd.read_csv("Optical Disorder - Sheet1.csv")
        medhis=medhis.set(df2.Medical_history)
        medbox = tk.Listbox(f2, listvariable=medhis, selectmode=MULTIPLE, width=40, height=8)
        medbox.grid(column=0, row=2, columnspan=2) 
        def select():
            reslist = list()
            selection =medbox.curselection()
            for i in selection:
                enter =medbox.get(i)
                reslist.append(enter)
            for val in reslist:
                val.append(reslist)

        f3 = tk.Frame(self,width = 1600,height = 500,relief=SUNKEN)
        f3.pack()
        
        btn=tk.Button(f3,text="Predict",command=lambda:controller.show_frame(PageTwo))
        btn.grid(column=0,row=1)


class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.configure(background = 'LightBlue')
        
      
        label1= tk.Label( self, text="Optical Disorder Detector",font=LARGE_FONT)
        label1.pack(pady=10,padx=10)
        
        homebutton= tk.Button(self, text= "Home",command=lambda:controller.show_frame(PageOne))
        homebutton.pack(pady=10,padx=10)
        
        backbutton= tk.Button(self, text="Back",command=lambda:controller.show_frame(PageTwo))
        backbutton.pack(pady=10,padx=10)

        label2=tk.Label(self, text="The patient is suffering from:")
        label2.pack(pady=10,padx=10)
        
        

        for F in(prediction1,prediction2)
        
            print(nb.predict())
        
                if(nb.severity==1)
                    photo= ImageTk.PhotoImage(Image.open('pred1.png'))
                    label_p1=tk.Label(self,image=photo)
                    label_p1.image=photo
                    label_p1.pack(pady=10,padx=10)

                if(nb.severity==2)
                    photo= ImageTk.PhotoImage(Image.open('pred2.png'))
                    label_p1=tk.Label(self,image=photo)
                    label_p1.image=photo
                    label_p1.pack(pady=10,padx=10)

                if(nb.severity==3)
                    photo= ImageTk.PhotoImage(Image.open('pred3.png'))
                    label_p1=tk.Label(self,image=photo)
                    label_p1.image=photo
                    label_p1.pack(pady=10,padx=10)

                if(nb.severity==4)
                    photo= ImageTk.PhotoImage(Image.open('pred4.png'))
                    label_p1=tk.Label(self,image=photo)
                    label_p1.image=photo
                    label_p1.pack(pady=10,padx=10)

                if(nb.severity==5)
                    photo= ImageTk.PhotoImage(Image.open('pred5.png'))
                    label_p1=tk.Label(self,image=photo)
                    label_p1.image=photo
                    label_p1.pack(pady=10,padx=10)
                    


        infobutton= tk.Button(self, text="info",command=lambda:controller.show_frame(PageThree))
        infobutton.pack(pady=10,padx=10)
        
        
        

class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.configure(background = 'LightBlue')
        
        button1 = tk.Button(self,text="Home",command=lambda:controller.show_frame(PageOne))
        button1.pack(pady=10,padx=10)

        button2 = tk.Button(self,text="Back",command=lambda:controller.show_frame(PageTwo))
        button2.pack(pady=10,padx=10)

        
        label=tk.Label(self,text="OPTICAL DISORDER DETECTOR",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        f2 = Frame(self,width = 800,height = 700,relief=SUNKEN)
        f2.pack()

        label4 = tk.Label(f2,text="Optical Disorder Detected:",font=('arial',18,'bold')) 
        label4.pack(pady=10,padx=10)
        
        print(nb.predict())
    

        f3 = Frame(self,width = 800,height = 700,relief=SUNKEN)
        f3.pack()
        label3 = tk.Label(f3,text="Recommended treatment:",font=('arial',18,'bold')) 
        label3.pack(pady=10,padx=10)

        print(nb.treatment())




       
       
app = Application()
app.mainloop()

