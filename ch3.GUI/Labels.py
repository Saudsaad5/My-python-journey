from tkinter import *

# Label = an eara widget that holds text and/or an image withen a window

window = Tk()
window.geometry("500x500")
window.title("Labels")
window.config(background='#FFBD73')


photo = PhotoImage(file='C:\\Users\\hason\\Documents\\Python\\ch3.GUI\\0773406e-c282-4ecd-8022-481c9768.png') # to uplode a pic

lable1 = Label   (window,text="Hello World",      # to create a label
                font=('Arial',40,'bold'),        # to change the font
                fg='#C4E1F6', bg='light blue',    # to set the colors
                 relief=RAISED, bd=10,            # to add a border
                 padx=20 , pady=20               # to add padding
)     
lable2 = Label(window, image=photo)              # to add the pic u uploaded
lable1.pack() # to display it
lable2.pack() # btw you can put them at the same lable
# to be more spicific you can use lable.place(x = 100, y = 100)

window.mainloop()