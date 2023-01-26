from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    login_details = website + " | " + username + " | " + password + "\n"
    with open("data.txt", mode="a") as login_data:
        login_data.write(login_details)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "georgi@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

window.mainloop()
