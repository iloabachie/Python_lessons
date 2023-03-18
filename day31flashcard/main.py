import tkinter as tk
import pandas as pd
import random as rd
import os

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000
words_to_learn = {}

def read_data():
    global word_dict, french_list
    try:
        df=pd.read_csv('D:/documents/Python lessons/AngelaYu/day31capstone/data/new_to_learn.csv')
    except FileNotFoundError:
        df = pd.read_csv('D:/documents/Python lessons/AngelaYu/day31capstone/data/french_words.csv')
    finally:
        word_dictionary = df.to_dict(orient='records')
        # print(word_dictionary)
        french_list = list(df.French)
        english_list = list(df.English)
        zipped = list(zip(french_list, english_list))
        word_dict = {a:b for a,b in zipped}
        # print(word_dict)
        

def reset_exit():
    try:
        os.remove('D:/documents/Python lessons/AngelaYu/day31capstone/data/new_to_learn.csv')
    except FileNotFoundError:
        exit()
    else:
        read_data()
    
    
def exit():
    windows.destroy()
    
    
def next_card():
    global french_word, flip_timer
    windows.after_cancel(flip_timer)
    french_word = rd.choice(french_list)
    canvas.itemconfig(front_text1, text='French', fill='black')
    canvas.itemconfig(front_text2, text=french_word, fill='black')
    canvas.itemconfig(card_image, image=front_image)
    flip_timer = windows.after(TIMER, flip_card)
    
    
def flip_card():
    global flip_timer
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(front_text1, text='English', fill='white')
    canvas.itemconfig(front_text2, text=word_dict[french_word], fill='white')
    
    
def known_words():
    global word_dict, french_list
    word_dict.pop(french_word)
    french_list.pop(french_list.index(french_word))
    next_card()
    # print(len(word_dict))
    to_learn = []
    for a, b in word_dict.items():
        new = {'French': a, 'English': b}
        to_learn.append(new)
    # print(to_learn)
    df = pd.DataFrame(to_learn)
    df.to_csv('D:/documents/Python lessons/AngelaYu/day31capstone/data/new_to_learn.csv', index=False)
    
 
def unknown_words():
    global words_to_learn, flip_timer
    words_to_learn.update({french_word: word_dict[french_word]})
    # print(len(words_to_learn))
    windows.after_cancel(flip_timer)
    flip_card()
    flip_timer = windows.after(TIMER, next_card)


windows = tk.Tk()
windows.title("Flash Card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(TIMER, flip_card)

wrong_img = tk.PhotoImage(file='D:/documents/Python lessons/AngelaYu/day31capstone/images/wrong.png')
wrong = tk.Button(image=wrong_img, highlightthickness=0, command=unknown_words)
wrong.grid(column=0, row=1)

right_img = tk.PhotoImage(file='D:/documents/Python lessons/AngelaYu/day31capstone/images/right.png')
right = tk.Button(image=right_img, highlightthickness=0, command=known_words)
right.grid(column=1, row=1)

reset_exit_button = tk.Button(text='Reset List/Exit App', command=reset_exit, highlightthickness=0)
reset_exit_button.grid(column=0, row=1, columnspan=2)

canvas = tk.Canvas(width=800, height=526)
front_image = tk.PhotoImage(file='D:/documents/Python lessons/AngelaYu/day31capstone/images/card_front.png')
back_image = tk.PhotoImage(file='D:/documents/Python lessons/AngelaYu/day31capstone/images/card_back.png')
card_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_text1 = canvas.create_text(400, 150, text='Title', fill='Black', font=('ariel', 40, 'italic'))
front_text2 = canvas.create_text(400, 260, text='Word', fill='Black', font=('ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

read_data()
next_card()



windows.mainloop()
