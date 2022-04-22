from tkinter import *
from quiz_brain import QuizBrain

TRUE_BUTTON = './images/true.png'
FALSE_BUTTON = './images/false.png'
THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="some q text", width=280,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_image = PhotoImage(file=TRUE_BUTTON)
        self.false_image = PhotoImage(file=FALSE_BUTTON)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.true_button = Button(image=self.true_image, height=90, width=90, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, height=90, width=90, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
