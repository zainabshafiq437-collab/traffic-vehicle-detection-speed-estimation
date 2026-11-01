import tkinter as tk

window = tk.Tk()
window.title("Zaina's Calculator")
window.geometry("350x450")
window.configure(bg="#1e1e2e")

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Can't divide by 0"
        else:
            result = "Select Operation"

        result_label.config(text=f"Result: {result}")
    except:
        result_label.config(text="Enter valid numbers!")

# Title
tk.Label(window, text="🧮 Simple Calculator", font=("Arial", 16, "bold"), bg="#1e1e2e", fg="white").pack(pady=20)

# Inputs
tk.Label(window, text="First Number", bg="#1e1e2e", fg="white").pack()
entry1 = tk.Entry(window, font=("Arial", 14), justify="center")
entry1.pack(pady=5)

tk.Label(window, text="Operation (+, -, *, /)", bg="#1e1e2e", fg="white").pack(pady=(10,0))
operation = tk.Entry(window, font=("Arial", 14), justify="center", width=10)
operation.insert(0, "+")
operation.pack(pady=5)

tk.Label(window, text="Second Number", bg="#1e1e2e", fg="white").pack(pady=(10,0))
entry2 = tk.Entry(window, font=("Arial", 14), justify="center")
entry2.pack(pady=5)

# Button
tk.Button(window, text="Calculate", command=calculate, bg="#89b4fa", font=("Arial", 12, "bold"), width=15).pack(pady=20)

# Result
result_label = tk.Label(window, text="Result will show here", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#a6e3a1")
result_label.pack(pady=10)

window.mainloop()
