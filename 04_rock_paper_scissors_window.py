import tkinter as tk
import random

window = tk.Tk()
window.title("Zaina's RPS Game")
window.geometry("450x400")
window.configure(bg="#1e1e2e")

# Scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    
    result = ""
    if user_choice == comp_choice:
        result = "Draw! 🤝"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You WIN! 🎉"
        user_score += 1
    else:
        result = "You LOSE! 😢"
        comp_score += 1
    
    status_label.config(text=f"You: {user_choice} | Computer: {comp_choice}\n{result}")
    score_label.config(text=f"Score -> You: {user_score} | Computer: {comp_score}")

# Title
tk.Label(window, text="🪨 Rock Paper Scissors ✂️", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="white").pack(pady=20)

# Buttons Frame
btn_frame = tk.Frame(window, bg="#1e1e2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🪨 Rock", command=lambda: play("Rock"), bg="#89b4fa", font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="📄 Paper", command=lambda: play("Paper"), bg="#a6e3a1", font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="✂️ Scissors", command=lambda: play("Scissors"), bg="#f9e2af", font=("Arial", 12, "bold"), width=10).pack(side=tk.LEFT, padx=5)

# Status
status_label = tk.Label(window, text="Choose your move!", font=("Arial", 12, "bold"), bg="#1e1e2e", fg="#cdd6f4", wraplength=400)
status_label.pack(pady=20)

score_label = tk.Label(window, text="Score -> You: 0 | Computer: 0", font=("Arial", 13, "bold"), bg="#1e1e2e", fg="white")
score_label.pack(pady=10)

window.mainloop()
