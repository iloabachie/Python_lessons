from tkinter import *
from tkinter import messagebox
from Pass_gen05 import pass_gen
import pyperclip
import json

# ---------------------- PASSWORD GENERATOR ------------------------ #

def delete_item():    
    try:
        with open('./day30-updatte/logs.json', 'r') as file: 
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='File Missing', message='Contact Support on 123456789')
    else:
        website = website_entry.get()
        is_ok = messagebox.askokcancel(title='Confirmation', message=f'Are you sure to delete data for {website}?')
        if is_ok:
            try:
                password_entry.delete(0, END)
                webaddress_entry.delete(0, END)
                username_entry.delete(0, END)
                website_entry.delete(0, END)
                webaddress = data[website.lower()]['webaddress']
                username = data[website.lower()]['username']
                password = data[website.lower()]['password']
                data.pop(website.lower())
            except KeyError as webname:
                messagebox.showinfo(title='Not found', message=f'{webname} data not found')
            else:
                
                with open('./day30-updatte/logs.json', 'w') as file:
                    json.dump(data, file, indent=4)          
                messagebox.showinfo(title='Deleted', message=f'Website: {website}\nWebAddress: {webaddress}\nUsername: {username}\nPassword{password}\nhas been removed')
                
def exit_window():
    window.destroy()

def generate_password():
    password_entry.delete(0, END)
    result = pass_gen()
    password_entry.insert(0, string=result)
    pyperclip.copy(result)

def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    webaddress_entry.delete(0, END)
    username_entry.delete(0, END)

def clear_website():
    website_entry.delete(0, END)
    global warning
    warning.destroy()

def search_data():
    try:
        with open('./day30-updatte/logs.json', 'r') as file: 
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='File Missing', message='Contact Support on 123456789')
    else:
        website = website_entry.get()
        try:
            password_entry.delete(0, END)
            webaddress_entry.delete(0, END)
            username_entry.delete(0, END)
            webaddress_entry.insert(0, string=data[website.lower()]['webaddress'])
            username_entry.insert(0, string=data[website.lower()]['username'])
            password_entry.insert(0, string=data[website.lower()]['password'])
        except KeyError as webname:
            messagebox.showinfo(title='Not found', message=f'{webname} data not found')
        

# ---------------------------- SAVE PASSWORD --------------------------
def save():
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()
    webaddress = webaddress_entry.get()
    new_data = {
        website.lower(): {
            'webaddress': webaddress,
            'username': username,
            'password': password
        }
    }
    
    if website == '' or username == '' or password == '' or webaddress == '':
        messagebox.showerror(title='Missing field', message='Please provide all details.')
    elif website == 'popup':
        global warning
        warning = Tk()
        warning.title('Careful')
        warning.config(padx=10, pady=10, bg='grey')
        warning_label = Label(warning, text='Do not visit', bg='white')
        warning_label.grid(column=0, row=0)
        warning_label.config(padx=5, pady=5)
        warning_button = Button(warning, text='Cancel', highlightthickness=0, command=clear_website)
        warning_button.grid(column=0, row=2)
        warning_button.config(padx=5, pady=5)

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Web address: {webaddress}\nUsername: {username}\nPassword: {password}')
        if is_ok:
            try:
                with open('./day30-updatte/logs.json', 'r') as file: 
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('./day30-updatte/logs.json', 'w') as file: 
                    json.dump(new_data, file, indent=4)
            else:
                with open('./day30-updatte/logs.json', 'w') as file: 
                    json.dump(data, file, indent=4, sort_keys=True)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                webaddress_entry.delete(0, END)
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

webaddress_label = Label(text='Web Address', bg='white')
webaddress_label.grid(column=0, row=3)
webaddress_label.config(padx=5, pady=5)

username_label = Label(text='Email/Username', bg='white')
username_label.grid(column=0, row=4)
username_label.config(padx=5, pady=5)


password_label = Label(text='Password', bg='white')
password_label.grid(column=0, row=5)
password_label.config(padx=5, pady=5)

search = Button(text='Search', highlightthickness=0, command=search_data, width=6)
search.grid(column=2, row=2)
search.config(padx=5, pady=5)

generate = Button(text='Generate', highlightthickness=0, command=generate_password)
generate.grid(column=2, row=5)
generate.config(padx=5, pady=5)

adds = Button(text='Save Password', highlightthickness=0, command=save, width=20)
adds.grid(column=1, row=6, columnspan=1)
adds.config(padx=5, pady=5)

clear = Button(text='Clear', highlightthickness=0, command=clear_fields, width=7)
clear.grid(column=2, row=6)
clear.config(padx=5, pady=5)

delete = Button(text='Delete', highlightthickness=0, command=delete_item, width=7)
delete.grid(column=0, row=6)
delete.config(padx=5, pady=5)

exit = Button(text='Exit', highlightthickness=0, command=exit_window, width=7)
exit.grid(column=2, row=0)
exit.config(padx=5, pady=5)

website_entry = Entry(width=35)
website_entry.insert(0, string="")
website_entry.focus()
website_entry.grid(column=1, row=2)

webaddress_entry = Entry(width=45)
webaddress_entry.insert(0, string="https://www.")
# webaddress_entry.focus()
webaddress_entry.grid(column=1, row=3, columnspan=2)

username_entry = Entry(width=45)
username_entry.insert(0, string="udemezue@gmail.com")
username_entry.grid(column=1, row=4, columnspan=2)

password_entry = Entry(width=35)
password_entry.insert(0, string='')
password_entry.grid(column=1, row=5)


window.mainloop()

