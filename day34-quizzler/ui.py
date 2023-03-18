from tkinter import *
from quiz_brain import QuizBrain





THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f'Score: 0/0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.score_label.config(padx=20, pady=20)
        
        false_img = PhotoImage(file='D:/documents/Python lessons/AngelaYu/day34-quizzler/images/false.png')
        self.f_button = Button(image=false_img, highlightthickness=0, command=self.wrong)
        self.f_button.grid(column=1, row=2)
        # self.f_button.config(pady=20)

        true_img = PhotoImage(file='D:/documents/Python lessons/AngelaYu/day34-quizzler/images/true.png')
        self.t_button = Button(image=true_img, highlightthickness=0, command=self.correct)
        self.t_button.grid(column=0, row=2)
        # self.t_button.config(pady=20)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.config(bg='white', highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text='Questions', fill='Black', width=280, font=('arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        try:
            new_question = self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question, text='Questions finished')
            self.t_button.config(state='disabled')
            self.f_button.config(state='disabled')
        else:
            self.canvas.itemconfig(self.question, text=new_question)

    def correct(self):
        global user_answer
        
        user_answer = (str(True)).lower()
        self.one = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        self.feedback()
            
        
    
    def wrong(self):
        
        user_answer = (str(False)).lower()
        self.one = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        self.feedback()            
            
        
            
    def feedback(self):
        
        if self.quiz.check_answer(user_answer):
            self.quiz.score -= 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
    
    # buttons can be disabled by button.config(state='disabled)