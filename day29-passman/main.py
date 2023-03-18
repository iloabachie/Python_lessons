from tkinter import *
from tkinter import messagebox
from Pass_gen05 import pass_gen
import pyperclip

# ---------------------- PASSWORD GENERATOR ------------------------ #
def generate_password():
    password_entry.delete(0, END)
    result = pass_gen()
    password_entry.insert(0, string=result)
    pyperclip.copy(result)
    
# ---------------------------- SAVE PASSWORD --------------------------
def save():
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()

    
    if website == '' or username == '' or password == '':
        messagebox.showerror(title='Missing field', message='Please provide all details.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Username: {username}\nPassword: {password}')
        if is_ok:
            with open('./day29-passman/password_log.txt', 'a') as file: 
                file.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title='Saved', message='Password log updated.')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_img = PhotoImage(file='./day29-passman/logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


website_label = Label(text='Website', bg='white')
website_label.grid(column=0, row=2)
website_label.config(padx=5, pady=5)


username_label = Label(text='Email/Username', bg='white')
username_label.grid(column=0, row=3)
username_label.config(padx=5, pady=5)


password_label = Label(text='Password', bg='white')
password_label.grid(column=0, row=4)
password_label.config(padx=5, pady=5)

generate = Button(text='Generate', highlightthickness=0, command=generate_password)
generate.grid(column=2, row=4)
generate.config(padx=5, pady=5)

adds = Button(text='Save Password', highlightthickness=0, command=save, width=20)
adds.grid(column=1, row=5, columnspan=2)
adds.config(padx=5, pady=5)

website_entry = Entry(width=45)
website_entry.insert(0, string="https://www.")
website_entry.focus()
website_entry.grid(column=1, row=2, columnspan=2)

username_entry = Entry(width=45)
username_entry.insert(0, string="udemezue@gmail.com")
username_entry.grid(column=1, row=3, columnspan=2)

password_entry = Entry(width=35)
password_entry.insert(0, string='type or generate pw')
password_entry.grid(column=1, row=4)



window.mainloop()

