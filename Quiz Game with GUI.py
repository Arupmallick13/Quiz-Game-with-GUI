# save as quiz_gui.py and run with: python quiz_gui.py
import tkinter as tk
from tkinter import messagebox
import random

QUESTIONS = [
    {"q": "What does CPU stand for?", "opts": ["Central Processing Unit", "Computer Power Unit", "Central Print Unit", "Control Program Utility"], "a": 0},
    {"q": "Which language is primarily used for web front-end?", "opts": ["Python", "C++", "JavaScript", "Rust"], "a": 2},
    {"q": "What is the value of binary 1010 in decimal?", "opts": ["10", "12", "8", "6"], "a": 0},
    {"q": "Which data structure uses FIFO?", "opts": ["Stack", "Queue", "Tree", "Graph"], "a": 1},
    {"q": "What does 'OOP' mean?", "opts": ["Object-Oriented Programming", "Only One Process", "Open Office Protocol", "Ordered Output Processing"], "a": 0},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        root.title("Quiz Game")
        root.geometry("600x320")
        self.score = 0
        self.q_index = 0
        self.questions = random.sample(QUESTIONS, len(QUESTIONS))  # shuffle
        self.var = tk.IntVar(value=-1)

        self.question_label = tk.Label(root, text="", wraplength=560, font=("Helvetica", 14))
        self.question_label.pack(pady=(20,10))

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value=i, font=("Helvetica", 12))
            rb.pack(anchor='w', padx=30)
            self.radio_buttons.append(rb)

        self.next_btn = tk.Button(root, text="Submit / Next", command=self.submit)
        self.next_btn.pack(pady=15)

        self.status_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12))
        self.status_label.pack()

        self.load_question()

    def load_question(self):
        if self.q_index >= len(self.questions):
            self.end_quiz()
            return
        q = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index+1}. {q['q']}")
        for i, opt in enumerate(q["opts"]):
            self.radio_buttons[i].config(text=opt)
        self.var.set(-1)

    def submit(self):
        sel = self.var.get()
        if sel == -1:
            messagebox.showinfo("Select", "Please choose an option before continuing.")
            return
        correct = self.questions[self.q_index]["a"]
        if sel == correct:
            self.score += 1
        # optional: immediate feedback
        # messagebox.showinfo("Result", "Correct!" if sel==correct else f"Wrong. Correct: {self.questions[self.q_index]['opts'][correct]}")

        self.q_index += 1
        self.status_label.config(text=f"Score: {self.score}")
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"You scored {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
