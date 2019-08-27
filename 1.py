import tkinter
from tkinter.ttk import *
from tkinter import *

window1 = tkinter.Tk()# for opening a window

window1.title("TKINTER TUTORIAL")       # for showing title in the top position.

#label1 = tkinter.Label(window1,text="Hello").pack()  # here, we created a label "label1" . The tkinter.Label function is assigned to it.

#inside the function ,we gives the window name where the object need to be shown "Here , window1 ". Then , in the "text" ,we gives the label to be shown.
# the .pack() is used to show the label in the window. 

window1.geometry('250x250') # to give the window size(height and width).here, "x" is just alphabet "x".not "*".


##################### LABEL WIDGET #######################

l1 = Label(window1,text="TESTING",font=("Arial",10)) # label "l1" created,shows in "window1",also the font size of text is set to  20 and given the font type.

l1.grid(column=0,row=2) # to set the position  and to show the label "l1".


#################### BUTTON WIDGET #######################

button1 = Button(window1,text="Enter")   # for button.
button1.grid(column=1,row=0)            # to set the position. 


button2 = Button(window1,text="Submit",bg="green",fg="yellow")  # For giving foreground and background colour . uses "bg" and "fg" respectively.
button2.grid(column=1,row=2)


def clicked():
    button1.configure(text="Button clicked")# here, the button1 will configures to "Button Clicked" when this function called by button2.
    
  
button2 = Button(window1,text="Submit",bg="orange",fg="red",command=clicked) # The "command " is used to link with a function.
button2.grid(column=1,row=2)



################### ENTRY WIDGET ###########################

# used to take inputs(like textbox) 

def show():
    res = input1.get() # we can use "get " function to get the user inputs.
    l2 = Label(window1,text=res,fg="red")  # here, The user input is  set to a label
    l2.grid(column=8,row=8)
    print(res)

input1 = Entry(window1,width=10)   # the width of the entrybox(textbox) is set.
input1.grid(column=1,row=7)

b3 = Button(window1,text="Click",command=show)
b3.grid(column=6,row=6)
                                       

################## COMBOBOX WIDGET #########################

# just like dropdownlist


combo1 = Combobox(window1)
combo1['values']= (1,2,3,4,5,"chennai","kerala")  # Here, the values needed to be shown given. we can give both string and integer values.
combo1.grid(column=5,row=15)



################# CHECKBUTTON     ##########################

# like checkbox

chk_state = BooleanVar() # The booleanVar is a tkinter  variable type. Here, it is used to set the "Checkbutton" already checked.
chk_state.set(True)  # the value is set to True, so the button will first displayed  as checked
chk = Checkbutton(window1,text="Select",var = chk_state)  # for checkbutton , var is used to indicate the above state
chk.grid(column=10,row=10)



################ RADIO BUTTON ##############################

# can only select one at a time

rad1 = Radiobutton(window1,text="python",value=1)
rad2 = Radiobutton(window1,text="Java",value=2)
rad3 = Radiobutton(window1,text="PHP",value=3)
rad1.grid(column=1,row=15)
rad2.grid(column=1,row=16)
rad3.grid(column=1,row=17)



############### SCROLLED TEXT WIDGET #########################

# REquired folowing class.
from tkinter import scrolledtext

t1 = scrolledtext.ScrolledText(window1,width=50,height=10)   # for scrolled text.
t1.insert('1.0',"WELCOME")


# Just Skip this.



############### MESSAGE BOX ##################################

from tkinter import messagebox

messagebox.showinfo("Message Title","Message content") # to show message in message box.

# showinfo is used for it, the message title is the title of the box and the message content is the content to be displayed in the box.

#example with function

def hit():
    a = 20
    messagebox.showinfo("Message Title","message content")

b5= Button(window1,text="Hit",command=hit)
b5.place(height=10,width=10)
#b5.grid(column=2,row=20)


################## SPINBOX ####################################


#Spinbox is a widely used widget as well. There are two tabs, the up and down scroll tabs present. This is how it differs from the scroll down widget. Here the static number will change over a certain range of values


spin= Spinbox(window1,from_=0,to=10,width=3)  # Here, the "from_" is the starting range and the "to" is the ending range.

spin.grid(column=1,row=22)





#################### GEOMETRY MANAGEMENT ######################


#All widgets in the Tkinter will have some geometry measurements. These measurements give you to organize the widgets and their parent frames, windows and so on.


# Tkinter has the following three Geometry Manager classes.

# pack():- It organizes the widgets in the block, which mean it occupies the entire available width. It’s a standard method to show the widgets in the window.

# grid():- It organizes the widgets in table-like structure.

# place():- It’s used to place the widgets at a specific position you want.



################## place() ################################

# Here is the list of possible options −

# anchor − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)

# bordermode − INSIDE (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.

# height, width − Height and width in pixels.

# relheight, relwidth − Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.

# x, y − Horizontal and vertical offset in pixels.


#eg:

# B5.place(bordermode=OUTSIDE, height=100, width=100,x=5,y=6)



################ ORGANIZING LAYOUTS AND WIDGETS ###################

#  To arrange the layout in the window, we will use Frame, class.

# Frame is used to create the divisions in the window. You can align the frames as you like with side parameter of pack() method.










