import tkinter

from numpy import short
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1#25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.1#20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # window.after_cancel(timer)
    global reps
    reps = 1000
    timer_label.config(text='Timer', fg=GREEN)
    check_mark.config(text='')
    canvas.itemconfig(timer_text, text='0:00')


def stop_timer():
    window.after_cancel(timer)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, timer_label, timer
    try:
        window.after_cancel(timer)
    except ValueError as error:
        print('value error:', error)
        pass
    else:
        print('no value error')
    finally:
        print('check what reps is', reps)
        work_sec = int(WORK_MIN * 60)
        short_break_sec = int(SHORT_BREAK_MIN * 60)
        long_break_sec = int(LONG_BREAK_MIN * 60)
        reps += 1

        if reps >= 1000:
            reps = 0
        else:
            if reps > 8:
                timer_label.config(text='Finished', fg=RED)
                canvas.itemconfig(timer_text, text='0:00')
            elif reps == 8:
                count_down(long_break_sec)
                timer_label.config(text='Long Break', fg=RED)
            elif reps % 2 == 0:
                count_down(short_break_sec)
                timer_label.config(text='Short Break', fg=PINK)
            else:
                count_down(work_sec)
                timer_label.config(text='Work work', fg=GREEN)
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def dummy():
    pass

def count_down(count):
    global reps, timer
    print(count)
    count_min = count // 60
    count_sec = count % 60
    if reps >= 1000:
        reps = 0
    else:
        if count_sec < 10:
            count_sec = f'0{count_sec}'

        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
        if count >= 0:            
            timer = window.after(1000, count_down, count - 1)
        else:
            start_timer()
            print('reps', reps)
            if reps % 2 == 0:
                ticks = '✔' * (reps // 2)
                print('ticks', ticks)
                check_mark.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=YELLOW)
# timer = window.after(1, dummy)

canvas = tkinter.Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='D:/documents/Python lessons/AngelaYu/day28-timer/tomato.png')
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 40, 'bold'))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 24, 'bold'))
timer_label.grid(column=1, row=0)
timer_label.config(padx=10, pady=10)

check_mark = tkinter.Label(fg='black', bg=YELLOW)
check_mark.grid(column=1, row=3)
check_mark.config(padx=10, pady=10)

startt = tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
startt.grid(column=0, row=2)
startt.config(padx=10, pady=10)

resett = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
resett.grid(column=2, row=2)
resett.config(padx=10, pady=10)

stopp = tkinter.Button(text='Stop', highlightthickness=0, command=stop_timer)
stopp.grid(column=2, row=1)
stopp.config(padx=10, pady=10)

window.mainloop()