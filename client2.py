from tkinter import *
from tkinter import scrolledtext

window = Tk()

lbl = Label(window, text="Name")
lbl.grid(column=0, row=0)

txt = Entry(window,width=20)
txt.grid(column=1, row=0)



window.geometry('350x500')





def clicked():
    print("Button was clicked!")
    print(txt.get())
    txt.delete(0, END)
    
btn = Button(window, text="Click Me", bg="blue", fg="white",command=clicked)
btn.grid(column=2, row=0)

scroll_txt = scrolledtext.ScrolledText(window,width=40,height=10)
scroll_txt.grid(column=0,row=1)






window.mainloop()

