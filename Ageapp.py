# Import three libraries 
# 1.datetime
# 2.tkinter
# 3.PIL import Image,ImageTk 

# Now lets define the person class


        
        

import tkinter as tk
import datetime
from PIL import Image,ImageTk

#Lets Create the window

window=tk.Tk()
window.title("Age Calculator App")
window.geometry("600x440")



#Now we'll create 4 labels each for name,year,month & date

name=tk.Label(text="Name")
name.grid(column=0,row=1)
year=tk.Label(text="Year")
year.grid(column=0,row=2)
month=tk.Label(text="Month")
month.grid(column=0,row=3)
date=tk.Label(text="Date")
date.grid(column=0,row=4)


#We define the input area for user to enter
nameEntry=tk.Entry()
nameEntry.grid(column=1,row=1)

yearEntry=tk.Entry()
yearEntry.grid(column=1,row=2)

monthEntry=tk.Entry()
monthEntry.grid(column=1,row=3)

dateEntry=tk.Entry()
dateEntry.grid(column=1,row=4)



#Now we define the function to get user input


def getInput():
    name=nameEntry.get()
    monkey=Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    
    textArea=tk.Text(master=window,height=10,width=30)
    textArea.grid(column=1,row=6)
    
    answer="Hey {monkey}!!!!. You are {age} years old!!!".format(monkey=name,age=monkey.age())
    
    textArea.insert(tk.END,answer)
    
    
# Now we create a button for the user to submit his/her input values

button=tk.Button(window,text="Calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=7)

class Person():
    
    def __init__(self,name,birthdate):
        self.name=name
        self.birthdate=birthdate
    def age(self):
        today=datetime.date.today()
        age=today.year-self.birthdate.year
        return age
        
        
# Now we'll add image to the app

image=Image.open('app2_image.jpg')
image.thumbnail((500,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)

