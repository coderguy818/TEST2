
from tkinter import *
Tk= (Tk)
window = Tk()
count = 0
def click():
    global count
    count+=1
    label.config(text=count)



window.title("Cool")
window.geometry("300x300")
button = Button(window,text= "Cool😎")
button.config(command=click)
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#224f13')
button.config(fg= '#f7f9fa')
button.config(activebackground='#175261')
image = PhotoImage(file='smiley.gif')
button.config(image=image)
button.config(compound='bottom')
label = Label(window,text=count)
label.config(font=('Monospace,50'))
label.pack()


button.pack()
label2 = Label()




window.mainloop()


