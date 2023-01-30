from tkinter import *


def convert():
    converted_distance = round(float(input_field.get()) * 1.609)
    converted_label.config(text=f"{converted_distance}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input_field = Entry(width=7)
input_field.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = Label(text=0)
converted_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
