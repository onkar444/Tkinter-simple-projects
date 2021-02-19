#importing the required libraries

import random
import tkinter as tk



#create a window for our game
window=tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x300")




#now  define the global variables that we are going to 
#use in our program
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""



#define the functions to get the users choice  to a number
def choice_to_number(choice):
    rps={"rock":0,"paper":1,"scissor":2}
    return rps[choice]
def number_to_choice(number):
    rps={0:"rock",1:"paper",2:"scissor"}
    return rps[number]


#define function to get the computers choice
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])



#Now we define the most important function
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You Win")
        USER_SCORE+=1
    else:
        print("Comp Wins")
        COMP_SCORE+=1
    
    text_area=tk.Text(master=window,height=12,width=30,bg="#ffff99")
    text_area.grid(column=0,row=4)
    answer=("Your Choice: {uc} \nComputer's Choice: {cc} \nYour Score: {u} \nComputer Score: {c}".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE))
    text_area.insert(tk.END,answer)

    
#now lets define three methods for the 3 different chocies
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
    
    
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
    
    

#Now lets define 3 buttons so that the user can click them
#and play the game

button1=tk.Button(text="  Rock  ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2=tk.Button(text=" Paper  ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3=tk.Button(text=" Scissor",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

#and we finally our favourite line;
window.mainloop()