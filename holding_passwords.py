from tkinter import *
from tkinter import messagebox
import random
import json


def find_password():
    try:
        with open("my_file.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="You haven't put any details yet\nso can't see anything")
    else:
        try:
            logins = data[entry1.get()]
        except KeyError:
            messagebox.showinfo(title="Wrong website", message="You didn't put any inforamtions\nabout this website...")
        else:
            email1 = logins["email"]
            password = logins["password"]
            messagebox.showinfo(title="Loggins", message=f"email: {email1}\npassword: {password}")


def genetrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(letters[char]) for char in range(random.randint(8, 10))]

    [password_list.append(symbols[char]) for char in range(random.randint(2, 4))]

    [password_list.append(numbers[char]) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password_done = "".join(password_list)
    entry3.insert(END, password_done)


def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askretrycancel(title="Would you like to continue?", message="You missed some gaps to fill.")
    else:
        try:
            with open("my_file.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("my_file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("my_file.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry1.delete(0, END)
            entry3.delete(0, END)


window = Tk()
window.title("Password Menager")
window.config(background="lightblue")
window.config(padx=50, pady=50)

website_lable = Label(text="Website: ")
website_lable.config(background="lightblue")
website_lable.grid(column=0, row=1)

email_lable = Label(text="Email/Username: ")
email_lable.config(background="lightblue")
email_lable.grid(column=0, row=2)

password_lable = Label(text="Password: ")
password_lable.config(background="lightblue")
password_lable.grid(column=0, row=3)

entry1 = Entry(width=33)
entry1.focus()
entry1.grid(column=1, row=1, columnspan=2)

entry2 = Entry(width=33)
entry2.insert(END, "Krzysztofcw2007@wp.pl")
entry2.grid(column=1, row=2, columnspan=2)

entry3 = Entry(width=33)
entry3.grid(column=1, row=3, columnspan=2)

generate_password_button = Button(text="Generate Password", command=genetrate_password)
generate_password_button.config()
generate_password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(columnspan=3, column=1, row=4)

search_button = Button(text="Search", command=find_password)
search_button.grid(columnspan=2, row=1, column=2)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, background="lightblue")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()
