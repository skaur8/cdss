from tkinter import *

root = Tk()



photo1= PhotoImage(file="1sized.png")
photo2=PhotoImage(file="2sized.png")
photo3=PhotoImage(file="5sized.png") 
label_p1=Label(root,image=photo1)
label_p2=Label(root,image=photo2)
label_p3=Label(root,image=photo3)

label1= Label( root, text="Eye Disorder Detector")
homebutton= Button(root, text= "Home")
backbutton= Button(root, text="Back")
nextbutton=Button(root, text=">>>>")

label2=Label(root, text="You may have the following")

label3=Label(root, text="Prediction 1")
label4=Label(root, text="Prediction 2")
label5=Label(root, text="Prediction 3")
label1.pack()
homebutton.pack()
backbutton.pack()
nextbutton.pack()
label2.pack()
label3.pack()
label_p1.pack()
label4.pack()
label_p2.pack()
label5.pack()
label_p3.pack()







root.mainloop()
