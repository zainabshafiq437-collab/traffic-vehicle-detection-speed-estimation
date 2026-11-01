import random
import string
import tkinter as tk

# Create Window - like pygame.display in Flappy Bird
window = tk.Tk()
window.title("Zaina's Password Generator")
window.geometry("400x300")
window.configure(bg="#1e1e2e")

def generate_password():
    # Get length from input box
    try:
        length = int(entry.get())
    except:
        length = 8  # Default length if error
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    # Show on label
    result_label.config(text=password)

# Title
title = tk.Label(window, text="🔐 Strong Password Generator", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="white")
title.pack(pady=20)

# Input Label
entry_label = tk.Label(window, text="Enter password length?", bg="#1e1e2e", fg="white", font=("Arial", 11))
entry_label.pack()

entry = tk.Entry(window, font=("Arial", 14), justify="center")
entry.insert(0, "8")
entry.pack(pady=10)

# Button
btn = tk.Button(window, text="Generate Password", command=generate_password, bg="#89b4fa", font=("Arial", 12, "bold"))
btn.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#a6e3a1", wraplength=350)
result_label.pack(pady=20)

# Keep window running - like game loop in pygame
window.mainloop()
