from tkinter import *


def button_clicked():
    print("I got clicked!")
    my_label.config(text=input_field.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=20)

# Button
button = Button(text="Press me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Don't press me")
button2.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)

# Always at the end of the code
window.mainloop()
