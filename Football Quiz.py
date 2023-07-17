import tkinter as tk
from tkinter import messagebox
import time

class FootballQuiz:
    def __init__(self, questions):
        self.questions = questions
        self.total_questions = len(questions)
        self.current_question = 0
        self.score = 0
        self.time_limit = 60
        self.timer_running = False
        self.root = tk.Tk()
        self.root.title("Football Quiz")
        self.label_question = tk.Label(self.root, wraplength=400, font=("Arial", 14))
        self.label_question.pack(pady=20)
        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)
        self.radio_buttons = []
        self.label_timer = tk.Label(self.root, text="Time Left: 0")
        self.label_timer.pack(pady=10)
        self.label_score = tk.Label(self.root, text="Score: 0")
        self.label_score.pack(pady=10)
        self.button_next = tk.Button(self.root, text="Next", command=self.next_question)
        self.button_next.pack(pady=10)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=20)
        self.start_timer()
        self.show_question()
        self.root.mainloop()

    def show_question(self):
        self.label_question.config(text=self.questions[self.current_question]['question'])
        self.clear_radio_buttons()
        for i, option in enumerate(self.questions[self.current_question]['options']):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack(pady=5)

    def clear_radio_buttons(self):
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()
        self.radio_buttons = []

    def next_question(self):
        selected_option = self.radio_var.get()
        if selected_option != -1:
            if self.questions[self.current_question]['answer'] == selected_option:
                self.score += 1
            self.current_question += 1
            if self.current_question == self.total_questions:
                self.end_quiz()
            else:
                self.show_question()
                self.update_score()
                self.reset_timer()
        else:
            messagebox.showwarning("Warning", "Please select an option.")

    def end_quiz(self):
        self.timer_running = False
        self.label_question.config(text="")
        self.clear_radio_buttons()
        self.button_next.config(state=tk.DISABLED)
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour score: {self.score}/{self.total_questions}")

    def update_score(self):
        self.label_score.config(text=f"Score: {self.score}")

    def update_timer(self):
        if self.time_limit > 0:
            self.time_limit -= 1
            self.label_timer.config(text=f"Time Left: {self.time_limit}")
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def reset_timer(self):
        self.time_limit = 60
        self.label_timer.config(text="Time Left: 60")

# Quiz Questions
questions = [
    {
        'question': "Which team won the FIFA World Cup in 2018?",
        'options': ["France", "Brazil", "Germany", "Spain"],
        'answer': 0
    },
    {
        'question': "Who is the all-time leading goal scorer in the UEFA Champions League?",
        'options': ["Lionel Messi", "Cristiano Ronaldo", "Raul Gonzalez", "Robert Lewandowski"],
        'answer': 1
    },
    {
        'question': "Which country has won the most Copa America titles?",
        'options': ["Brazil", "Argentina", "Uruguay", "Colombia"],
        'answer': 2
    },
    {
        'question': "Which player has won the most Ballon d'Or awards?",
        'options': ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
        'answer': 0
    },
    {
        'question': "Which team has won the most UEFA European Championships?",
        'options': ["Spain", "Germany", "Italy", "France"],
        'answer': 2
    },
    {
        'question': "Who is the all-time leading goal scorer for the Brazilian national team?",
        'options': ["Pele", "Romario", "Ronaldo", "Neymar"],
        'answer': 0
    },
    {
        'question': "Which club has won the most UEFA Champions League titles?",
        'options': ["Real Madrid", "Barcelona", "Bayern Munich", "AC Milan"],
        'answer': 0
    },
    {
        'question': "Which player has scored the most goals in a single Premier League season?",
        'options': ["Alan Shearer", "Thierry Henry", "Luis Suarez", "Mohamed Salah"],
        'answer': 3
    },
    {
        'question': "Who is the all-time leading goal scorer for the German national team?",
        'options': ["Miroslav Klose", "Gerd Muller", "Jurgen Klinsmann", "Michael Ballack"],
        'answer': 0
    },
    {
        'question': "Which player has won the most FIFA World Player of the Year awards?",
        'options': ["Lionel Messi", "Cristiano Ronaldo", "Zinedine Zidane", "Ronaldinho"],
        'answer': 0
    }
]

quiz = FootballQuiz(questions) 
 
