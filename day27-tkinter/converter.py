from tkinter import *

window1 = Tk()
window1.title('Converter')
# window1.minsize(width=300, height=150)
window1.config(padx=20, pady=20)

miles = Label(text='miles')
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

kilo = Label(text='km')
kilo.grid(column=2, row=1)
kilo.config(padx=10, pady=10)

equiv = Label(text='is equal to')
equiv.grid(column=0, row=1)
equiv.config(padx=10, pady=10)

ans = Label(text='0')
ans.grid(column=1, row=1)
ans.config(padx=10, pady=10)

# def button_click():  
#     # global ans
#     # ans.destroy()
#     km = float(entry.get()) * 1.60934
#     ans = Label(text=km)
#     ans.grid(column=1, row=1)
#     ans.config(padx=10, pady=10)


def button_click():
    if entry.get() == '':
        ans.config(text='enter value')
    else:
        km = round(float(entry.get()) * 1.60934, 2)
        ans.config(text=km)
    
calculate = Button(text='Calculate', command=button_click)
calculate.grid(column=1, row=2)
calculate.config(padx=10, pady=10)

def button_clear():
    ans.config(text=0)
    
clear = Button(text='Reset', command=button_clear)
clear.grid(column=0, row=2)
clear.config(padx=10, pady=10)

entry = Entry(width=15)
entry.insert(END, string='')
entry.grid(column=1, row=0)


window1.mainloop()