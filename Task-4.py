import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissor")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.user_score = 0
        self.comp_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Rock Paper Scissors", font=("Arial", 20, "bold")).pack(pady=20)
        self.score_label = tk.Label(self.root, text="User: 0  |  Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)
        self.result_display = tk.Label(self.root, text="Choose your move!", font=("Arial", 14, "italic"), fg="blue")
        self.result_display.pack(pady=20)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Rock", width=10, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Paper", width=10, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Scissors", width=10, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)

        tk.Button(self.root, text="Reset Game", fg="red", command=self.reset_game).pack(pady=20)

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        
        if user_choice == comp_choice:
            result = f"It's a tie! Both chose {user_choice}"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = f"You Win! {user_choice} beats {comp_choice}"
            self.user_score += 1
        else:
            result = f"You Lose! {comp_choice} beats {user_choice}"
            self.comp_score += 1

        self.result_display.config(text=result)
        self.score_label.config(text=f"User: {self.user_score}  |  Computer: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="User: 0  |  Computer: 0")
        self.result_display.config(text="Game Reset. Choose your move!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()