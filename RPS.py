# Import Required Library
from tkinter import *
import random
#for color gradient
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
# Set title
  
# here, image option is used to
# set image on button

root.title("Rock_Paper_Scissor_Game")
 
# Computer Value
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
 
# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
 
# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = c_v)
    button_disable()
 
# If player selected paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Paper           ")
    l3.config(text = c_v)
    button_disable()
 
# If player selected scissor
def isscissor():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Scissor         ")
    l3.config(text = c_v)
    button_disable()
 
# Add Labels, Frames and Button
Label(root,
      text = "Rock Paper Scissor",
      font = "normal 20 bold",
      fg = "dark blue").pack(pady = 30)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "Player              ",
           font = 20)
 
l2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
 
l3 = Label(frame, text = "Computer", font = 20)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = rgb_hack((91, 193, 137)),
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 30)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text = "Rock",
            font = 20, width = 7,
            command = isrock)
 
b2 = Button(frame1, text = "Paper ",
            font = 20, width = 7,
            command = ispaper)
 
b3 = Button(frame1, text = "Scissor",
            font = 20, width = 7,
            command = isscissor)
 
b1.pack(side = LEFT, padx = 20)
b2.pack(side = LEFT,padx = 20)
b3.pack(padx = 20)
 
Button(root, text = "Reset Game",
       font =  "normal 10 bold", fg = "white",
       bg =rgb_hack((37, 85, 102)), command = reset_game).pack(pady = 30)
 
# Execute Tkinter
root.mainloop()
