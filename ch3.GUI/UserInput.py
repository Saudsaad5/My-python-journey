from tkinter import *

def delete():
    entry.delete(0,END)

def submit():
    username = entry.get()
    print(username)


window = Tk()

submit = Button(window,text="submit",command=submit)
delete = Button(window,text="Delete", command=delete)

entry = Entry()
entry.config(font=('', 20))
entry.config(bg='#FFAD60')
entry.pack()
submit.pack()
delete.pack()
 

window.mainloop()