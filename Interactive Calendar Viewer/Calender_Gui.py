from  tkinter import *
import  calendar
root=Tk()
root.geometry("550x600")
root.title("Calender ")
img=PhotoImage(file='calendar_icon.png')
root.iconphoto(False, img)

root.config(background='gray')


def show():
    r=Toplevel()
    r.geometry("550x600")
    r.config(bg='gray')
    n=var.get()
    txt = calendar.calendar(n)
    l1 = Label(r, text=txt, font=("consolas 10 bold "),bd=4, relief=SUNKEN,fg='black', bg='light blue')
    l1.pack()


lab=Label(root, text="Calender",fg='cyan', bg='orange',font=("time",20,'bold'), bd=6, relief=RIDGE,padx=40)

lab.place(x=166, y=10)


e=Label(root,text="Enter Year",font=("time",20,'bold'), relief=SUNKEN, padx=25,fg='red')
e.place(x=30,y=140)
var=IntVar()
en=Entry(root, textvariable=var,font=("time",19,'bold'), relief=RAISED,bd=4)

en.place(x=240, y=140)
#
bt=Button(root, text="Click", command= show,font=("time",20,'bold'), padx=50,relief=RIDGE,bd=5, fg='blue', bg='pink')
bt.place(x=180, y=220)


l=Label(root, image=img, padx=300,bd=7,relief=SOLID)
l.place(x=180, y=350)


root.mainloop()
