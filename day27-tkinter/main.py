import tkinter

window = tkinter.Tk()

window.title('first GUI')
window.minsize(width=500, height=300)
# add padding to window
window.config(padx=20, pady=20)

#creating a label

my_label = tkinter.Label(text='I am a label', font=('Arial', 16, 'bold'))
my_label.pack() # difficult to control
my_label.place(x=200, y=100) #rigid in place
my_label.grid(column=0, row=0) # relative to others.  define what should be on top best option
my_label.config(padx=10, pady=10)

# change label methods
my_label['text'] = 'New Text'
my_label.config(text='new text')

def button_click():
    print('i got clicked')
    my_label.config(text='you clicked it didnt you')
    my_label.config(text=input.get())

# adding entries
input = tkinter.Entry(width=10)
input.grid(column=3, row=3)
print(input.get())

# creating buttons
button = tkinter.Button(text='Print', command=button_click)
button.grid(column=1, row=1)





window.mainloop()