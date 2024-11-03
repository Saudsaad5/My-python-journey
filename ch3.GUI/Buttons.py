from tkinter import *

 # a function to use when clicking the button
count =0
def click():
   global count
   count += 1
   Label.config(text=count)
    

window = Tk()
window.geometry('500x500')
button = Button(window,text='click me !!!') # creating a button
button.config(command=click)  # to link the button to the function
button.config(font=('Ink Free',20,'bold'))
button.config(bg='#9B7EBD')
button.config(fg='#FFE1FF')


Label = Label(window, text=count)
Label.config(font=('Monospace',50))
Label.pack()
button.pack() # to place the button


window.mainloop()