from tkinter import *
from quiz_brain import QuizzBrain


# constants
THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 15, "italic")
FONT_SCORE = ("Arial", 10, "bold")
GREEN = "#BFEA7C"
RED =  "#D04848"

# class of ui
class QuizInterface:
    def __init__(self, quiz_brain: QuizzBrain):
        def when_true():
            """function which define checkmark button behavior
            """
            answer = quiz_brain.check_answer("True")
            self.feedback(answer)                
                
        def when_false():
            """function which define cross button behavior
            """
            answer = quiz_brain.check_answer("False")
            self.feedback(answer)
        
        # argument passed to show on canvas
        self.quiz_brain = quiz_brain
        
        # main window
        self.window = Tk()
        self.window
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question", 
                                                     font=FONT_QUESTION, width=280)
        # self.canvas.config()
        self.canvas.grid(column=0, row=1, columnspan=2)
        
        # buttons
        checkmark_img = PhotoImage(file="images/true.png")
        self.checkmark = Button(image=checkmark_img, command=when_true,
                                highlightthickness=0)
        self.checkmark.grid(column=0, row=2)
        
        cross_img = PhotoImage(file="images/false.png")
        self.cross = Button(image=cross_img, command=when_false, 
                            highlightthickness=0)
        self.cross.grid(column=1, row=2)
        
        # label score
        self.score = 0
        self.questions = 0
        self.score_label = Label(text=f"Score: {self.score} / {self.questions}", font=FONT_SCORE,
                                 bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        
        # new question
        self.next_question()
        
        # mainloop
        self.window.mainloop()
        
    def next_question(self):
        question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=question)
        self.canvas.config(bg="white")

    def feedback(self, answer):
        self.questions += 1
        if answer: # check if user was right
            self.canvas.config(bg=GREEN)
            self.score += 1 
        else:
            self.canvas.config(bg=RED)
        self.score_label.config(text=f"Score: {self.score} / {self.questions}")
        self.window.after(1500, self.next_question)
