import tkinter as tk
import random

window = tk.Tk()
window.title("Zaina's Flappy Bird - Easy")
window.geometry("400x600")
window.configure(bg="#70c5ce")

canvas = tk.Canvas(window, width=400, height=520, bg="#70c5ce", highlightthickness=0)
canvas.pack()

# Bird easy physics
bird_y = 250
bird_velocity = 0
gravity = 0.25  # pehle 0.5 tha, ab slow hai
score = 0
game_over = False

bird = canvas.create_oval(50, bird_y, 80, bird_y+30, fill="#FFEB3B", outline="black", width=2)
eye = canvas.create_oval(65, bird_y+5, 75, bird_y+15, fill="black")
beak = canvas.create_polygon(80, bird_y+12, 95, bird_y+15, 80, bird_y+18, fill="orange", outline="black")

pipes = []
pipe_gap = 200  # pehle 150 tha, ab gap bada hai

def create_pipe():
    h = random.randint(80, 280)
    top = canvas.create_rectangle(400, 0, 460, h, fill="#73BF2E", outline="black", width=2)
    bottom = canvas.create_rectangle(400, h+pipe_gap, 460, 600, fill="#73BF2E", outline="black", width=2)
    pipes.append((top, bottom, h))

def flap(event=None):
    global bird_velocity
    if not game_over:
        bird_velocity = -6  # thora tez upar
        print("FLAP!")

def update():
    global bird_y, bird_velocity, score, game_over
    
    if game_over:
        return

    bird_velocity += gravity
    bird_y += bird_velocity
    
    canvas.coords(bird, 50, bird_y, 80, bird_y+30)
    canvas.coords(eye, 65, bird_y+5, 75, bird_y+15)
    canvas.coords(beak, 80, bird_y+12, 95, bird_y+15, 80, bird_y+18)

    for top, bottom, h in pipes[:]:
        canvas.move(top, -2, 0)  # slow speed
        canvas.move(bottom, -2, 0)
        coords = canvas.coords(top)
        if coords[2] < 0:
            canvas.delete(top)
            canvas.delete(bottom)
            pipes.remove((top, bottom, h))
            score += 1
            score_label.config(text=f"Score: {score} | Click / SPACE for flap")

        if (50 < coords[2] and 80 > coords[0]):
            if bird_y < h or bird_y+30 > h+pipe_gap:
                game_over = True
                score_label.config(text=f"GAME OVER! Score: {score} - Press R")

    if bird_y > 520 or bird_y < 0:
        game_over = True
        score_label.config(text=f"GAME OVER! Score: {score} - Press R")

    if not game_over:
        window.after(16, update)

def restart(event=None):
    global bird_y, bird_velocity, score, game_over, pipes
    if not event or event.keysym.lower() == 'r' or event.keysym == 'R':
        bird_y = 250
        bird_velocity = 0
        score = 0
        game_over = False
        for top, bottom, h in pipes:
            canvas.delete(top)
            canvas.delete(bottom)
        pipes.clear()
        score_label.config(text="Score: 0 | Click / SPACE for flap")
        update()
        spawn_pipe()

def spawn_pipe():
    if not game_over:
        create_pipe()
        window.after(2000, spawn_pipe)  # 2 sec baad naya pipe

# IMPORTANT - Ye line game ko clickable banati hai
window.focus_set()
window.bind("<space>", flap)
window.bind("<Button-1>", flap)
window.bind("<r>", restart)
window.bind("<R>", restart)

score_label = tk.Label(window, text="Score: 0 | CLICK / SPACE se Bird Udao!", font=("Arial", 12, "bold"), bg="#70c5ce", fg="black")
score_label.pack(pady=5)

tk.Label(window, text="TIP: Baar baar CLICK karo, girne mat do!", bg="#70c5ce").pack()

spawn_pipe()
update()

window.mainloop()
