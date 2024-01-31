from tkinter import *


# opening tag

window = Tk()
# title
window.title("Desktop App")

# body

# change the apps size

window.geometry('500x500')
# show text
lbl = Label(window, text = "Hello how are you ")
lbl.grid(column=0, row=0)
# style text
style = Label(window, text = "style with large ", font=("Arial Bold", 30))
style.grid(column=0, row=2)

# button

btn = Button(window, text = "Click me")
btn.grid(column=0, row=3)



# style button

btn2 = Button(window, text = "color btn", bg="green", fg = "white")
btn2.grid(column=0, row=4)


# apply function on button

txt = Entry(window, width=10)
txt.grid(column=0, row=5)
def clicked():
    res = "Welcome to " + txt.get()
    style.configure(text=res)


btn3 = Button(window, text = "functional btn", command=clicked)
btn3.grid(column=1, row=5)


# closing tag
window = mainloop()