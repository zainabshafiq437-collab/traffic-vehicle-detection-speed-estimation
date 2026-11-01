import tkinter as tk

window = tk.Tk()
window.title("Zaina's Unit Converter")
window.geometry("400x350")
window.configure(bg="#1e1e2e")

def convert_speed():
    try:
        kmh = float(entry_kmh.get())
        # Formula: km/h to m/s
        ms = kmh * 1000 / 3600
        result_label.config(text=f"{kmh} km/h = {ms:.2f} m/s")
    except:
        result_label.config(text="Please enter a valid number!")

def convert_back():
    try:
        ms = float(entry_ms.get())
        kmh = ms * 3600 / 1000
        result_label.config(text=f"{ms} m/s = {kmh:.2f} km/h")
    except:
        result_label.config(text="Please enter a valid number!")

# Title
tk.Label(window, text="🚗 Speed Converter", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="white").pack(pady=20)

# km/h to m/s
tk.Label(window, text="Enter Speed in km/h", bg="#1e1e2e", fg="white").pack()
entry_kmh = tk.Entry(window, font=("Arial", 14), justify="center")
entry_kmh.insert(0, "72")
entry_kmh.pack(pady=5)

btn1 = tk.Button(window, text="Convert to m/s", command=convert_speed, bg="#89b4fa", font=("Arial", 11, "bold"))
btn1.pack(pady=5)

# m/s to km/h
tk.Label(window, text="Enter Speed in m/s", bg="#1e1e2e", fg="white").pack(pady=(15,0))
entry_ms = tk.Entry(window, font=("Arial", 14), justify="center")
entry_ms.pack(pady=5)

btn2 = tk.Button(window, text="Convert to km/h", command=convert_back, bg="#a6e3a1", font=("Arial", 11, "bold"))
btn2.pack(pady=5)

# Result
result_label = tk.Label(window, text="", font=("Arial", 13, "bold"), bg="#1e1e2e", fg="#f9e2af")
result_label.pack(pady=20)

window.mainloop()
