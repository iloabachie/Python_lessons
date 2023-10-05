from tkinter import *
from tkinter import messagebox
from Pass_gen05 import pass_gen
import pyperclip # py -m pip install pyperclip
import sqlite3

con = sqlite3.connect(r'D:\Documents\Python lessons\AngelaYu\day30-sqlite3\data_base.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS passwords(Website TEXT PRIMARY KEY, Address TEXT, Username TEXT, Password TEXT)')

def delete_item():   
    website = website_entry.get() 
    is_ok = messagebox.askokcancel(title='Confirmation', message=f'Are you sure to delete data for {website}?')
    if is_ok:        
        try:
            primary_key = f'{website}'
            cur.execute('SELECT * FROM passwords WHERE Website = ?', (primary_key,))
            row = cur.fetchone()     
            # print(row) 
            # print("********************")      
            if row == None:
                raise Exception
            cur.execute('DELETE FROM passwords WHERE Website = ?', (primary_key,))
            con.commit()             
        except:
            messagebox.showinfo(title='Not found', message=f'{website} data not found')  
        else:
            messagebox.showinfo(title='Deleted', message=f'Website: {website} removed\nWebAddress: {row[1]}\nUsername: {row[2]}\nPassword{row[3]}\nhas been removed')
        finally:     
            clear_fields()
                
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

def clear_website():  # not in use
    website_entry.delete(0, END)
    global warning
    warning.destroy()

def search_data():
    website = website_entry.get()
    try:
        cur.execute(f'SELECT * FROM passwords') # WHERE website = {website}')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print('************')
        # actual code here
        primary_key = f'{website}'
        cur.execute('SELECT * FROM passwords WHERE Website = ?', (primary_key,))
        row = cur.fetchone()
        print(row)
        print("*************")
        if row == None and len(website) > 0:
            raise Exception        
    except:
        messagebox.showerror(title='Data Missing', message=f'{website} data not found')
    else:        
        clear_fields()
        #show output  
        if row: 
            website_entry.insert(0, string=row[0])             
            webaddress_entry.insert(0, string=row[1])
            username_entry.insert(0, string=row[2])
            password_entry.insert(0, string=row[3])
        

# ---------------------------- SAVE PASSWORD --------------------------
def save():
    password = password_entry.get()
    username = username_entry.get()
    website = website_entry.get()
    webaddress = webaddress_entry.get()
       
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
            cur.execute(f'INSERT OR IGNORE INTO passwords VALUES ("{website}", "{webaddress}", "{username}", "{password}")')
            con.commit()  
            clear_fields()
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

username_label = Label(text='Username', bg='white')
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

cur.close()
con.close()


