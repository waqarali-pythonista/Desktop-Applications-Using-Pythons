import tkinter as tk
import webbrowser



def open_google_maps():
    location = entry.get()
    url = f"https://www.google.com/maps/place/{location}"
    webbrowser.open(url)

app = tk.Tk()
img=tk.PhotoImage(file='icon.png')
app.title("Google Maps")

app.iconphoto(False, img)
app.geometry("270x450")
app.config(bg='#bce9ee')

label = tk.Label(app, text="Enter  Location ", fg='white', bg='gray', font="Gothic 19 bold", bd=7, relief=tk.RIDGE)
label.pack(pady=12)

entry = tk.Entry(app, fg='orange', bg='#594227', font=("Arial 15 bold "),bd=6, relief=tk.FLAT)
entry.pack(pady=25)

button = tk.Button(app, text="Open in Google Maps", bg='black',font=(" arial 12 bold"),bd=3,fg='cyan',command=open_google_maps, activebackground='red',activeforeground='yellow')
button.pack(pady=10)

img=tk.PhotoImage(file='map.png')
lab_img=tk.Label(app, image=img)
lab_img.place(x=25, y=250)

app.mainloop()
