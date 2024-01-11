from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT=("Arial",20,"italic")
GAME_OVER_CLR='#CD8D7A'

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):

        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR ,pady=50,padx=50)
        self.label=Label(text=f'Score:{self.quiz.score}',font=FONT,bg=THEME_COLOR,fg='white')
        self.label.grid_configure(row=0,column=1)
        self.canvas=Canvas(height=250,width=300,bg='white',highlightthickness=0)
        self.ques_text=self.canvas.create_text(150,125,width=280,text="some question text", fill='black',font=FONT)
        self.canvas.grid_configure(row=1,column=0,columnspan=2,pady=50)
        right_photo_path=PhotoImage(file='images/true.png')
        self.right_button=Button(image=right_photo_path,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid_configure(row=2,column=0)
        wrong_button_path=PhotoImage(file='images/false.png')
        self.wrong_button=Button(image=wrong_button_path,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid_configure(row=2,column=1)

        self.next_question()




        self.window.mainloop()

    def next_question(self):
       self.canvas.configure(bg='white')
       self.label.configure(text=f'Score:{self.quiz.score}')
       if self.quiz.still_has_questions():
           new_ques_text = self.quiz.next_question()
           self.canvas.itemconfig(self.ques_text,text=new_ques_text)
       else:
           self.canvas.itemconfig(self.ques_text, text='You have reached the end of the game')
           self.canvas.configure(bg=GAME_OVER_CLR)
           # disabling the buttons
           self.right_button.configure(state='disabled')
           self.wrong_button.configure(state='disabled')

    def true_pressed(self):

        result=self.quiz.check_answer('true')

        if result:
            self.turn_green()
        else:
            self.turn_red()

        self.window.after(1000,self.next_question)



    def false_pressed(self):

        result=self.quiz.check_answer('false')

        if result:
            self.turn_green()
        else:
            self.turn_red()

        self.window.after(2000,self.next_question)


    def turn_red(self):
        self.canvas.configure(bg='red')

    def turn_green(self):
        self.canvas.configure(bg='green')